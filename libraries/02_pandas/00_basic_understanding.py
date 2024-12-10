'''
Introduction to Pandas: 
    Pandas is a Python library used for data manipulation and analysis. 
    It provides data structures and functions to efficiently handle structured 
    data, including tabular data such as spreadsheets and SQL tables.

Key Features of Pandas:

Series:
    A one-dimensional labeled array of values.

DataFrame:
    A two-dimensional table of values with rows and columns.

Data Manipulation:
    Pandas provides various functions for filtering, sorting, and grouping data.

Data Analysis:
    Pandas integrates well with other popular data analysis libraries in Python, 
    such as NumPy, Matplotlib, and Scikit-learn.

Basic Pandas Operations:

Creating a DataFrame:
    You can create a DataFrame from a dictionary, a list of lists, or by reading 
    data from a file.

Viewing Data: 
    You can use the head(), tail(), and info() functions to view the 
    first few rows, last few rows, and summary information about the data.

Filtering Data:
    You can use conditional statements to filter data based on specific conditions.

Sorting and Grouping Data:
    You can use the sort_values() and groupby() functions to sort and group data.
'''

import pandas as pd

# Create a dictionary
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}

# Create a DataFrame
df = pd.DataFrame(data)

# View the first few rows of the DataFrame
print(df.head())

# Filter the DataFrame to include only rows where Age is greater than 30
print(df[df['Age'] > 30])