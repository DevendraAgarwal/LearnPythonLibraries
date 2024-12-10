# Necessary Functions

import pandas as pd

df = pd.read_csv("diabetes.csv")

'''
You can view the first few or last few rows of a DataFrame using the 
.head() or .tail() methods, respectively. You can specify the number of rows 
through the n argument (the default value is 5).
'''
df.head()
df.tail(n = 10)

'''
The .describe() method prints the summary statistics of all numeric columns, 
such as count, mean, standard deviation, range, and quartiles of numeric columns.
It gives a quick look at the scale, skew, and range of numeric data.
'''
df.describe()

'''
You can also modify the quartiles using the percentiles argument. Here, 
for example, we’re looking at the 30%, 50%, and 70% percentiles of the numeric 
columns in DataFrame df.
'''
df.describe(percentiles=[0.3, 0.5, 0.7])

'''
Often, practitioners find it easy to view such statistics by transposing them with the .T attribute.
'''
df.describe().T

'''
The .info() method is a quick way to look at the data types, missing values, 
and data size of a DataFrame. Here, we’re setting the show_counts argument to 
True, which gives a few over the total non-missing values in each column. 
We’re also setting memory_usage to True, which shows the total memory usage of 
the DataFrame elements. When verbose is set to True, it prints the full summary 
from .info(). 
'''

df.info(show_counts==True, memory_usage=True, verbose=True)

'''
Calling the .columns attribute of a DataFrame object returns the column names in 
the form of an Index object. As a reminder, a pandas index is the address/label 
of the row or column.
'''
df.columns
list(df.columns)