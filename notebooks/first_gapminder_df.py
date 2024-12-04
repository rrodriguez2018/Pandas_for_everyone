import pandas as pd

#df = pd.read_csv('./gapminder-main/inst/extdata/gapminder.tsv', sep='\t')
df = pd.read_csv('./data/gapminder.tsv', sep='\t')

#print(type(df)) # gives the type of object df is
#print(df.shape) # number of rows, number of columns
#print(df.columns) # prints the names of the columns
#print(df) # print out the actual dataframe (if large, only head and tail is shown)
#print(df.dtypes) # prints out the types for each column
#print(df.info()) # prints out more information about each column

#print(df.head()) # just prints out the first 5 rows of data
#print(df.tail()) # just prints out the last 5 rows of data

country_df = df["country"]
# print(country_df.head())
# print(country_df)
# subset = df[['country', 'continent','year']]
# print(subset
# print(type(country_df)) # prints <class 'pandas.core.series.Series'>
country_df_list = df[['country']] # using double brackets, we now get back a dataframe object instead
# print(country_df_list)
#print(type(country_df_list)) # when we inquire about the type, we confirm it is a dataframe
#print(df.country) # using dot notation can also get you the series(column or 'vector') as long as column name not odd
# print(df.loc[0]) # this gets the first row (python counts from 0)
#print(df.loc[99]) # this gets the 100th row info
# print(df.loc[[0, 99, 999]]) # gets the three rows passed in.
# loc mehtod gets rows by the row index labels (which could be the default numbers) but iloc mehtod gets rows by row numbers only.
# print(df.iloc[-1]) # this gets the last row. with iloc we can pass -1
# print(df.iloc[[0, 99, 999]])
# subset = df.loc[:,['year','pop']] # this gets the columns subset. To just use integers, try iloc instead!
# print(subset)
# rows_subset = df.loc[[0, 99], :] # remember: the left side are the rows and the right side are the columns.
# print(rows_subset)
# small_range = list(range(5))
# print(small_range)
# print(df.iloc[small_range]) # this gets the columns specified by integers from newly created list!
# print(df.iloc[:,small_range]) # this gets the specified dataframe vectors(columns) per created list "small_range"
# second_small_range = list(range(3, 6))
# print(df.iloc[:, second_small_range])
# third_small_range = list(range(0, 6, 2)) # we can pass a third argument, step, to specify how to increment between start and stop
# print(df.iloc[:, third_small_range])
# third_small_range = df.iloc[:, 0:6:2]
# print(third_small_range) # we could also replace the range method (generator) with simple : and do slicing like this! (same result!)
# third_small_range = df.iloc[:, 0:6:] # if we don't specify step, we get default step=1.
# third_small_range = df.iloc[:, 0::2] # if we don't specify stop, we get from 0 to stop=default(end) with step of 2
# third_small_range = df.iloc[:, ::2] # we get same as above (start=0 by default)
# third_small_range = df.iloc[:, ::] # we get everything (default to include from 0 to end in step of 1)
# print(third_small_range)
# print(df.loc[42,'country']) # we can also slice row (first entry) from selected column 'country' like so. Watch out to use iloc for numbers!
# print(df.iloc[[0, 99, 999],[0, 3, 5]]) # to slice both rows AND columns, use iloc and specify each row/column as needed. 
# using loc with actual column names sometimes is better (easier code review) than iloc and vector indexes which don't mean anything.
# print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])

# groupby() method:
# take a look at the 'training' folder! it has all sections. 
# multi_group_var = (
#     df
#     .groupby(['year', 'continent'])
#     [['lifeExp','gdpPercap']]
#     .mean()
# )
# print(multi_group_var) # one style of printing data where column titles don't align...
# flat = multi_group_var.reset_index()
# print(flat) # this prints nice table. with aligned column titles!

# print(df.groupby('continent')['country'].nunique()) # use nunique() to get qty of unique numbers on a series
# print(df.groupby('continent')['country'].value_counts()) # we get the count of entries per country

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
# print(global_yearly_life_expectancy)

import matplotlib.pyplot as plt
global_yearly_life_expectancy.plot()

plt.show()