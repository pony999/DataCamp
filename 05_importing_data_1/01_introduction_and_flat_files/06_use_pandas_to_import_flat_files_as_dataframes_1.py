"""
Using pandas to import flat files as DataFrames (1):
In the last exercise, you were able to import flat files containing columns with different datatypes as numpy arrays.
However, the DataFrame object in pandas is a more appropriate structure in which to store such data and, thankfully, we
can easily import files of mixed data types as DataFrames using the pandas functions read_csv() and read_table().
"""


# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = r'../_datasets/titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())