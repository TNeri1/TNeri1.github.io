#%%
import pandas as pd
import altair as alt

dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv')


# %%
# how many unique names

dat.name.unique()
dat.name.nunique()
# 7354 unique names

# %%
dat.query("name == 'Trevor'").year.max() #2015
dat.query("name == 'Trevor'").year.min() #1929
dat.query("name == 'Trevor'").year.nunique() #72

# Write a short sentence describing your results

# %%
# Sum all the years for each name (groupby()).
# Create a new DataFrame for the totals.
# Write a query that filters the total data to the max and min.
# Create a markdown table with the information.
# A. to_markdown() requires the tabulate package.
# B. to_markdown() with arguments showindex and floatformat
# C. Guidance on floatforma

# Which name is used themost and which is used the least?

dat.groupby(['name']).agg(sum = ('Total','sum')).reset_index()

# reset_index helps drops column names at standard data table look

# %%

"""
This takes names and finds the sum total of those names and a sum total
of the names within the state of Oregon
"""

dat_total = (dat
    .groupby(['name'])
    .agg(sum_total = ('Total','sum'),
         sum_oregon = ('OR','sum'))
    .reset_index())

# dat_total.sort_values('sum')
#%%
dat_total.query("sum_total == @dat_total.sum_total.max()")
#%%
print(dat_total
    .query("sum_total == @dat_total.sum_total.min()")
    .to_markdown(showindex = False)) #index or showindex (if index is broke)

# %%


