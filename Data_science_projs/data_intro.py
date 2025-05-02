import pandas as pd
import numpy as np

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Viewing data
print(df.head())      # First 5 rows
print(df.describe())  # Summary statistics

# Selecting data
print(df['Name'])     # Get column
print(df.iloc[1])     # Get row by position
print(df.loc[0])      # Get row by index

# Filtering
print(df[df['Age'] > 28])  # Rows where Age > 28

# Adding columns
df['Senior'] = df['Age'] > 30

# Handling missing data
df.dropna()          # Drop rows with missing values
df.fillna(value=0)   # Fill missing values with 0

# Grouping and aggregation
print(df.groupby('City')['Age'].mean())  # Average age by city

# Reading/writing data
df = pd.read_csv('data.csv')  # Read from CSV
df.to_excel('output.xlsx')    # Write to Excel