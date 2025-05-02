import pandas as pd
import datetime
#import pathlib
#
#print (pathlib.Path.cwd())
fifa_data = pd.read_csv("./data_cleaning/fifa21_raw_data.csv")
#print(fifa_data)

print(fifa_data.info())
print(fifa_data[fifa_data["Height"].notna()])
print(fifa_data["Weight"])

# converting height and weight to numbers

temp = fifa_data["Height"].str.split("'") #this gives a series of lists
'''
note that the .str is an accessor which gives access to the various methods to manipulate
strings. Recall that from observation via the .info() the datatypes for non numeric types
are "objects". not strings or str.. thats why we need an accessor

'''

'''
converting the weight to numbers. 

'''
new_series = temp.apply(lambda arr : int(arr[0]) * 12) + temp.apply(lambda arr : int(arr[1].strip("\"")))
print(new_series)

'''
converting the weight 

'''

dirty_weight = fifa_data["Weight"]

#view inique values in the series and the frequency of each
print(dirty_weight.unique(), "\n", dirty_weight.value_counts(dropna=False))

def remove_lbs_from_weight(new_series: pd.Series):
    '''this function assumes that the input series is has no missing values
        and that the weight is of the form "***lbs"
        we aim to remove this and just have only digits in the series

    '''
    #new_series.str.strip("lbs") 
    cleaned_weight = new_series.str.slice_replace(start=-3, repl="")
    print(cleaned_weight)
    return cleaned_weight.apply(lambda x: int(x))

def Over_10yrs(players_df : pd.DataFrame):
    '''
    this function checks which players have been playing at a club for over 10 years
    using the "joined" column
    '''
    print(players_df["Joined"].unique()) # view the unique entries in the series
    
    # we are extracting a group of 4 numbers with regular expressions )
    yearsJoined = players_df["Joined"].str.extract(r'(\d{4})') #Note that str. extract returns a dataframe not a series because it is designed to extract multiple capture groups
    print(type(yearsJoined)) # should give a dataframe
    print(yearsJoined.info()) #note that the default colimn label of "0" has been assigned to our dataframe

    #   to get a series
    yearsJoined = yearsJoined[0]
    #print(yearsJoined.unique())
    
    #   to convert the entries to integers
    #yearsJoined = yearsJoined.apply(lambda x: int(x)) OR
    #yearsJoined = yearsJoined.astype(int) #or
    yearsJoined = pd.to_numeric(yearsJoined)

    return (datetime.date.today().year - yearsJoined) > 10

def clean_wage(players_df : pd.DataFrame):
    dirty_wages = players_df["Wage"] #we should get a series here
    # view before cleaning
    print(dirty_wages.unique(), dirty_wages.shape)
    # proceed to extract using regular expressions
    cleaned_wages = dirty_wages.str.extract(r"€(\d{1,3})K?") #returns a dataframe
    cleaned_wages = cleaned_wages[0] # get the series
    pd.to_numeric(cleaned_wages) #convert the entries to intergers
    # print(cleaned_wages.unique())
    return cleaned_wages

  



print(remove_lbs_from_weight(dirty_weight).unique())
print(fifa_data[Over_10yrs(fifa_data)])
print(clean_wage(fifa_data).unique())
print(fifa_data["Release Clause"].head(1216))


#print(temp.dtype)
#print(temp.to_list())
#fifa_data["Height"] = int(fifa_data["Height"].convert_dtypes) 
#fifa_data["Weight"] = int(fifa_data["Weight"])

#print(fifa_data.info())
