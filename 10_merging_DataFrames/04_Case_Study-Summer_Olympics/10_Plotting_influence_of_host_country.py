"""
Plotting influence of host country:
This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the
influence of being a host country.

Instructions:
*   Create a Series called change by extracting the 'Change' column from influence.
*   Create a bar plot of change using the .plot() method with kind='bar'. Save the result as ax to permit further
    customization.
*   Customize the bar plot of change to improve readability:
*   Apply the method .set_ylabel("% Change of Host Country Medal Count") toax.
*   Apply the method .set_title("Is there a Host Country Advantage?") to ax.
*   Apply the method .set_xticklabels(editions['City']) to ax.
*   Reveal the final plot using plt.show().
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load editions
editions_file_path = '../_datasets/Summer_Olympics/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'
editions = pd.read_csv(editions_file_path, sep='\t')
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Import hosts and reshaped
hosts = pd.read_csv('../_datasets/Summer_Olympics/hosts.csv')
reshaped = pd.read_csv('../_datasets/Summer_Olympics/reshaped.csv')
# Set influences
merged = pd.merge(reshaped, hosts, how='inner')
influence = merged.set_index('Edition').sort_index()
# *****************************************************************

# Extract influence['Change']: change
change = influence['Change']
# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()