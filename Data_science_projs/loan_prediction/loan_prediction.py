'''
useful tips
* high income earning individuals should have more chances of receiving loans
* loan amount - the lesser the amount, the higher the chance for approval
* loan term - the shorter the duration, the more likely the approval
* previous history should have a huge impact on the approval. those that have history defaulting should have lesser chances of approval
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# good practice is to manipulate copies of the actual data
train_data = pd.read_csv("./train_u6lujuX_CVtuZ9i.csv").copy()
test_data = pd.read_csv("./test_Y3wMUE5_7gLdaTN.csv").copy()

# inspect the train data
print(" Training data information - columns and datatypes: \n")
train_data.info()
print(train_data.shape)

print(" Test data information - columns and datatypes: \n")
test_data.info(),
print(test_data.shape)



#inspecting the test data, starting from the loan status

print(" the unique values we have in loan status are: \n", train_data['Loan_Status'].value_counts()"
#print(train_data.describe())

#train_data.groupby('Loan_Status').size()
train_data.groupby('Loan_Status').size().plot(kind='bar', color=['red', 'green'])
plt.show()

'''
trying to make sense of the indivdual data (univariate analysis)

train_data.describe() already gave a hint that we have a coulple of missing values in some numerical columns

categorical columns (order doesn't matter here)- gender, married=yes/no,  self_employed=Yes/No, credit_history=1/0,
ordinal columns (order matters) -  property_area=urban/rural(urban preferrable), dependents (the less the better), Education (Graduate preferrable), credit_history=1/0,
numerical columns - loan amount, loan amount term, income, coapplicant income, applicant income
'''

gender_counts = train_data['Gender'].value_counts()
married_counts = train_data['Married'].value_counts()
selfemp_counts = train_data['Self_Employed'].value_counts()

#plot catagorical variables 
fig_1 = plt.figure("categorical data") #create a figure
genderPlot, marriedPlot, selfempPlot = fig_1.subplots(3,1)

# Plot Gender data
genderPlot.bar(gender_counts.index, gender_counts.values, color=['red', 'green'])
genderPlot.set_title('Gender')
genderPlot.set_xlabel('Gender')
genderPlot.set_ylabel('Count')

for i, value in zip(gender_counts.index, gender_counts.values):
    genderPlot.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

# Plot Married data
marriedPlot.bar(married_counts.index, married_counts.values, color=['blue', 'orange'])
marriedPlot.set_title('Married')
marriedPlot.set_xlabel('Marital Status')
marriedPlot.set_ylabel('Count')

for i, value in zip(married_counts.index, married_counts.values):
    marriedPlot.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

# Plot Self-Employed data
selfempPlot.bar(selfemp_counts.index, selfemp_counts.values, color=['purple', 'yellow'])
selfempPlot.set_title('Self Employed')
selfempPlot.set_xlabel('Self Employment Status')
selfempPlot.set_ylabel('Count')

# annotate each bar with its values
for i, value in zip(selfemp_counts.index,selfemp_counts.values):
    selfempPlot.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

'''
plotting ordinal variables: property_area, dependents, education, credit_history
'''
fig2 = plt.figure("ordinal data") #create a figure
row1, row2 = fig2.subplots(2,2)

propertyAreaPlot, dependentsPlot = row1
educationPlot, credit_historyPlot = row2

propertyAreaCounts = train_data['Property_Area'].value_counts()
educationCounts = train_data['Education'].value_counts()
creditHistoryCounts = train_data['Credit_History'].value_counts()
dependentsCounts = train_data['Dependents'].value_counts()

#plot property area
propertyAreaPlot.bar(propertyAreaCounts.index, propertyAreaCounts.values, color=['red', 'green', 'blue'])
propertyAreaPlot.set_title('Property Area')
propertyAreaPlot.set_xlabel('Property Area')
propertyAreaPlot.set_ylabel('Count')

#plot education
educationPlot.bar(educationCounts.index, educationCounts.values, color=['red', 'green', 'blue'])
educationPlot.set_title('Education')
educationPlot.set_xlabel('Education')
educationPlot.set_ylabel('Count')

#plot dependents
dependentsPlot.bar(dependentsCounts.index, dependentsCounts.values, color=['red', 'green', 'blue'])
dependentsPlot.set_title('Dependents')
dependentsPlot.set_xlabel('Dependents')
dependentsPlot.set_ylabel('Count')

#plot   credit history
credit_historyPlot.bar(creditHistoryCounts.index, creditHistoryCounts.values, color=['red', 'green', 'blue'])
credit_historyPlot.set_title('Credit History')
credit_historyPlot.set_xlabel('Credit History')
credit_historyPlot.set_ylabel('Count')

plt.tight_layout()
plt.show()



#data clean up and missing value imputation

'''
 We will change the 3+ in dependents variable to 3 to make it a numerical variable.
 We will also convert the target variable’s categories into 0 and 1 so that we can make it numerical since
   logistic regression takes only numeric values as input. We will replace N with 0 and Y with 1."
'''
# Replace '3+' with 3 in the 'Dependents' column
train_data['Dependents'] = train_data['Dependents'].replace('3+', 3)
test_data['Dependents'] = test_data['Dependents'].replace('3+', 3)

# Replace 'N' with 0 and 'Y' with 1 in the 'Loan_Status' column
train_data['Loan_Status'] = train_data['Loan_Status'].replace({'N': 0, 'Y': 1})

#Bivariate analysis:
numeric_data = train_data.select_dtypes(include=["int64", "float64"])
matrix = numeric_data.corr() 
print("correlation matrix: ", "\n", matrix)
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(matrix, vmax=.8, square=True, cmap="BuPu");
plt.show()


print("observe that the LoanAmount and Applicant Income are Correlated \n\n\n")

# handling missing vaalues
print("train_data before imputation: ", "\n", train_data.isnull().sum(), "\n")
print("test_data before imputation: ", "\n", test_data.isnull().sum(), "\n")

# observe that there are missing values in: 
# 1. LoanAmount
# 2. Loan_Amount_Term
# 3. Credit_History
# 4. Dependents
# 5. Self_Employed
# 6. Gender
# 7. married

# filling missing values

'''
For columns like Gender, Self_Employed, or Dependents, where the data represents categories,
 the mode is a logical choice because it preserves the most common category in the data.
'''



# MANUALLY FILLING VALUES


# Indexing with [0]: Since mode() always returns a pandas Series, even if there is only one mode, [0] is used to access the first element of the resulting Series.
train_data['Gender'] = train_data['Gender'].fillna(train_data['Gender'].mode()[0])
train_data['Dependents'] = train_data['Dependents'].fillna(train_data['Dependents'].mode()[0])
train_data['Self_Employed'] = train_data['Self_Employed'].fillna(train_data['Self_Employed'].mode()[0])
train_data['Credit_History'] = train_data['Credit_History'].fillna(train_data['Credit_History'].mode()[0])
train_data['Married'] = train_data['Married'].fillna(train_data['Married'].mode()[0])
# numerical columns with continuopus data

#loan amount term has 360 occuring the most(mode), we can fill with that
train_data["LoanAmount"] = train_data["LoanAmount"].fillna(train_data["LoanAmount"].median()) #we fill with the median here
train_data["Loan_Amount_Term"] = train_data["Loan_Amount_Term"].fillna(train_data["Loan_Amount_Term"].mode()[0])

# verify no nulls
print("train data after imputation: ", "\n", train_data.isnull().sum())
#xx = zip(train_data["LoanAmount"].value_counts().index, train_data["LoanAmount"].value_counts().values)
#print(train_data["Loan_Amount_Term"].value_counts(), "\n")
#for i in xx:
#    print(i, end = " ")

# fill missing values in test data

test_data["Gender"] = test_data['Gender'].fillna(train_data['Gender'].mode()[0])
test_data['Dependents'] = test_data['Dependents'].fillna(train_data['Dependents'].mode()[0]) 
test_data['Self_Employed'] = test_data['Self_Employed'].fillna(train_data['Self_Employed'].mode()[0]) 
test_data['Credit_History'] = test_data['Credit_History'].fillna(train_data['Credit_History'].mode()[0])
test_data['Loan_Amount_Term'] = test_data['Loan_Amount_Term'].fillna(train_data['Loan_Amount_Term'].mode()[0])
test_data['LoanAmount'] = test_data['LoanAmount'].fillna(train_data['LoanAmount'].median())


'''
# FILLING MISSING VALUES USING SKLEARN IMPUTER (PIPELINE) to ensure consistency



# Define the preprocessing steps for each column
categorical_columns = ['Gender', 'Married', 'Dependents', 'Self_Employed', 'Credit_History',  'Loan_Amount_Term']
numeric_columns = ['LoanAmount']
preprocessor = ColumnTransformer(
    transformers=[
        ('categorical_imputer', SimpleImputer(strategy='most_frequent'), categorical_columns),
        ('numerical_imputer', SimpleImputer(strategy='median'), numeric_columns),
    ],
    remainder='passthrough'  # Keep other columns as-is
)

# Create a pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])
# Separate the target variable from the training data since target variable
# is not in the test data
X_train = train_data.drop(columns=['Loan_Status'])  # Features only
y_train = train_data['Loan_Status']  # output variable

# Ensure the test data does not include the target column
X_validate = test_data  # Features only (test data typically doesn't have the target column)

# Fit the pipeline on the training features (without the target variable)
pipeline.fit(X_train)  # pipeline learns and computes the needed parameters for imputing

#print("before pipeline \n train_data")
#X_train.info()
#print("before pipeline \n test_data")
#X_validate.info()

print("Before pipeline \n train_data \n", train_data)
#train_data.info()
print("Before pipeline \n test_data \n", test_data)

# Transform both training and test features
X_train_transformed = pipeline.transform(X_train)
X_validate_transformed = pipeline.transform(X_validate)
print(X_train_transformed, "\n", X_validate_transformed)

# Convert the transformed data back to DataFrames
X_train_temp= pd.DataFrame(X_train_transformed, columns=X_train.columns)
test_data_temp= pd.DataFrame(X_validate_transformed, columns=X_validate.columns)

# Explicitly cast numeric columns back to their original types
numeric_columns = X_train.select_dtypes(include=['float64', 'int64']).columns #get a list of columns with numeric datatype

X_train_temp[numeric_columns] = X_train[numeric_columns].apply(pd.to_numeric)
test_data_temp[numeric_columns] = X_validate[numeric_columns].apply(pd.to_numeric)

X_train = X_train_temp
test_data = test_data_temp
# Reattach the target variable to the training data if needed
train_data = pd.concat([X_train, y_train], axis=1)
'''

# Verify data has been properly transformed
print("after filling in missing values \n", "Train data \n", train_data.isnull().sum(), "\n", "Test data", test_data.isnull().sum())

print("after pipeline \n train_data")
train_data.info()
print("after pipeline \n test_data")
test_data.info()


'''
using logistic regression - a classification algorithm that is used to predict the probability of an event occurring, such as loan approval
Basically, this can be used to predict binary outcomes
such a customer's loan request should be approved or not
'''

#since the loan ID is not needed, we can drop it
train_data = train_data.drop(columns=['Loan_ID'])
test_data = test_data.drop(columns=['Loan_ID'])

# Split the train  data into features (X) and target variable (y) 
#as this is required by the model
xTrain = train_data.drop(columns=['Loan_Status'])
yTrain = train_data['Loan_Status']

'''
since the logistic regression model is purely numeric, there is a need
to convert categorical columns to some form of numeric representation
utilizing dummies

dummies will utilize the unique values in a categotical column to create new columns
for each unique value (using encoding). Each new column will have a 1 or 0 value representing
whether the record falls in that category or not.
eg. Gender will be split into Gender_Male and Gender_Female - records with 1 under Gender_Male, are male. others will be 0 under Gender_Male
'''
'''
print("Before dummies \n train_data \n", train_data)
#train_data.info()
print("Before dummies \n test_data \n", test_data)
#test_data.info()
'''
xTrain = pd.get_dummies(xTrain) #leave the  drop_first=True for now
test_data = pd.get_dummies(test_data) #leave the  drop_first=True for now
'''
print("after dummies \n train_data")
xTrain.info()
print("after dummies \n test_data")
test_data.info()
'''


#print(xTrain.columns, "\n", test_data.columns)


'''
in order to evaluate the performance of our model,
we need to split the training data (with the output variable known)
into training and validations sets before testing with data that we do not
know the output variable.
'''
# split the data into training and testing sets
X_train, X_validate, y_train, y_validate = train_test_split(xTrain, yTrain, test_size=0.2)

#next we fit the model
model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_validate) #make predictions on the test set
print("accuracy score is: \n", accuracy_score(y_validate, y_pred)) #print the accuracy score
#...

'''
Now making predictions for the test data
'''
pred_output = model.predict(test_data)

print("\n \npredicted output is: \n", pred_output)

# recall that we need our Loan Status in Y or N therefore



