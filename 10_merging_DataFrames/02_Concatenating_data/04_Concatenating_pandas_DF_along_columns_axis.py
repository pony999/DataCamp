"""
Concatenating pandas DataFrames along column axis:

The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To
make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.

In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly
versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null
values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more
detail in later exercises).

The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and
weather_mean respectively, and pandas has been imported as pd.

Instructions:
*   Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
*   Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
*   Print the new DataFrame weather.
"""


# Import pandas
import pandas as pd

# Read names files
weather_max = pd.read_csv('../_datasets/quarterly_max_temp.csv', index_col=[0])
weather_mean = pd.read_csv('../_datasets/monthly_mean_temp.csv', index_col=[0])
# ****************************************************

# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max, weather_mean], axis=1, sort=True)

# Print weather
print(weather)
