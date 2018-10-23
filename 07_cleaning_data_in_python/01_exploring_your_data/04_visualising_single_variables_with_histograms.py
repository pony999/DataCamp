"""
Visualizing single variables with histograms:
Up until now, you've been looking at descriptive statistics of your data. One of the best ways to confirm what the
numbers are telling you is to plot and visualize the data.

You'll start by visualizing single variables using a histogram for numeric values. The column you will work on in this
exercise is 'Existing Zoning Sqft'.

The .plot() method allows you to create a plot of each column of a DataFrame. The kind parameter allows you to specify
the type of plot to use - kind='hist', for example, plots a histogram.

In the IPython Shell, begin by computing summary statistics for the 'Existing Zoning Sqft' column using the .describe()
method. You'll notice that there are extremely large differences between the min and max values, and the plot will need
to be adjusted accordingly. In such cases, it's good to look at the plot on a log scale. The keyword arguments logx=True
or logy=True can be passed in to .plot() depending on which axis you want to rescale.

Finally, note that Python will render a plot such that the axis will hold all the information. That is, if you end up
with large amounts of whitespace in your plot, it indicates counts or values too small to render.

INSTRUCTIONS:
* Import matplotlib.pyplot as plt.
* Create a histogram of the 'Existing Zoning Sqft' column. Rotate the axis labels by 70 degrees and use a log scale for
  both axes.
* Display the histogram using plt.show().
"""


# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read the file into a DataFrame: df
df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

"""
Output comment:
While visualizing your data is a great way to understand it, keep in mind that no one technique is better than another. 
As you saw here, you still needed to look at the summary statistics to help understand your data better. You expected a 
large amount of counts on the left side of the plot because the 25th, 50th, and 75th percentiles have a value of 0. The 
plot shows us that there are barely any counts near the max value, signifying an outlier.
"""
