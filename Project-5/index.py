import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np


data = pd.read_csv("googleplaystore.csv")
# print(data)


# Questions:
# 1. Display Top 5 Rows of The Dataset
print(data.head())

# 2. Check the Last 3 Rows of The Dataset
print(data.tail(3))


# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
shapes = data.shape
print("No of rows are: ", shapes[0])
print("No of columns are: ", shapes[1])

# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

print(data.info())
# 5. Get Overall Statistics About The Dataframe
print(data.describe(include='all'))
# 6. Total Number of App Titles Contain Astrology
print(data.columns)
print(data['App'])
print(data[data["App"].str.contains("Astrology", case= False)])
# 7. Find Average App Rating

print(data.columns)
print(data['Rating'].mean())
# 8.  Find Total Number of Unique Category

print(data['Category'].value_counts())
print(len(data['Category'].unique()))
print(data['Category'].nunique())
# 9. Which Category Getting The Highest Average Rating?
print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False))

# 10. Find Total Number of App having 5 Star Rating
print(data.columns)
print(len(data[data['Rating'] == 5.0]))

# 11. Find Average Value of Reviews
print(data.columns)
print(data['Reviews'].dtype)
print(data[data['Reviews'] == "3.0M"])
data['Reviews'] = data['Reviews'].replace("3.0M", 3.0)
print(data['Reviews'].dtype)
data['Reviews'] = data['Reviews'].astype('float')
print(data['Reviews'].mean())

# 12. Find Total Number of Free and Paid Apps
print(data.columns)
# free = len(data[data['Type'] == 'Free'])
# paid = len(data[data['Type'] == 'Paid'])
# print(f"Paid: {paid}, Free: {free}")
print(data['Type'].value_counts())

# 13.  Which App Has Maximum Reviews?
print(data.columns)
print(data[data['Reviews'].max() == data['Reviews']]['App'])

# 14. Display Top 5 Apps Having Highest Reviews

print(data.columns)
index_value = data['Reviews'].sort_values(ascending=False).head().index
print(data.iloc[index_value]['App'])
# 15. Find Average Rating of Free and Paid Apps
print(data.columns)
print(data.groupby('Type')['Rating'].mean())

# 16. Display Top  5 Apps Having Maximum Installs
print(data['Installs'])
data['Installs_1'] = data['Installs'].str.replace(',','')
data['Installs_1'] = data['Installs_1'].str.replace('+','')
print(data)
index_value = data['Installs_1'].sort_values(ascending=False).head().index
print(data.iloc[index_value]['App'])