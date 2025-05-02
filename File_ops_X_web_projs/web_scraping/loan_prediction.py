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



# good practice is to manipulate copies of the actual data
train_data = pd.read_csv("./loan_prediction/train_u6lujuX_CVtuZ9i.csv").copy()
test_data = pd.read_csv("./loan_prediction/test_Y3wMUE5_7gLdaTN.csv").copy()

# inspect the train data
print(train_data.info(),"\n", train_data.shape, "\n ", test_data.info(), "\n", test_data.shape)
print(train_data.columns, "\n", train_data.dtypes)

#inspecting the test data, starting from the loan statuscd 

train_data['Loan_Status'].value_counts()
train_data.groupby('Loan_Status').size()
train_data.groupby('Loan_Status').size().plot(kind='bar', color=['red', 'green'])
plt.show(block=True)