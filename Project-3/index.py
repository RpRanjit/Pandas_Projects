import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("adult.csv")

# Top 10 rows of datasets
print(data.head(10))

# Lst 10 rows of datasets
print(data.tail(10))

# Shape of our datasets (No of rows and columns)
shapes = data.shape
print(shapes)

# Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requiremen
print(f"No of rows: {shapes[0]}")
print(f"No of columns: {shapes[1]}")
print(data.info())

#  Fetch Random Sample From the Dataset (50%)
half_data_sets = data.sample(frac= 0.50)
# If you use the same random_state value, you’ll get the same sampled rows every time you run the code.
half_data_sets = data.sample(frac= 0.50, random_state= 100)
print(half_data_sets)

# Check Null Values In The Dataset
print(data.isnull())
print(data.isnull().sum())
# /for it we can also use visualize form
# sns.heatmap(data.isnull())
# plt.show()



# Perform Data Cleaning [ Replace '?' with NaN ]
print(data.isin(["?"]).sum())
print(data.columns)

import numpy as np
data['workclass'] = data["workclass"].replace("?",np.nan)
data['occupation'] = data["occupation"].replace("?",np.nan)
data['native-country'] = data["native-country"].replace("?",np.nan)
print(data.isin(["?"]).sum())

print(data.isnull().sum())
# sns.heatmap(data.isnull())
# plt.tight_layout()
# plt.show()


# Drop all The Missing Values
# first find the percentage of missing values
pct_missing_values = data.isnull().sum() * (100/len(data))
print(pct_missing_values)
old_data = data.shape[0]
data.dropna(how='any', inplace= True)
new_data = data.shape[0]
print(old_data - new_data )

# Check For Duplicate Data and Drop Them
print(data.duplicated().any())
# if True
before_drop_duplicate = data.shape[0]
data = data.drop_duplicates()
after_drop_duplicate = data.shape[0]
print(before_drop_duplicate-after_drop_duplicate)

# Get overall statisctcs od our datasets

print(data.describe())
# for both numeric and statical columns
print(data.describe(include="all"))

print(data.columns)
print(data['education'].unique())
print(data["educational-num"].unique())

# to check if they represent same data
print(data.groupby('education')['educational-num'].unique())
# each group represent single unique numbers so they represent same son we can drop one column

# Drop the columns educational-num, capital-gain and capital-loss
# /we are dropping capital-gain and capital-loss because its 75% are 0

data = data.drop(['educational-num', 'capital-gain', 'capital-loss'], axis=1)
print(data.columns)

# Univariate analysis
# taking one variable at a time and performing analysis on it
# first on age column
# What is the dirtribution of age column
print(data['age'].describe())
# for distribution we use histogram
# data['age'].hist()
# plt.show()

#  Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
# with out using between method
required_age = data[(data['age'] >=17) & (data['age'] <=48)]
print(required_age)
print(data[data['age'].between(17, 48,inclusive='both')])

# What is the distribution of orkclass column
print(data['workclass'].describe())
# plt.figure(figsize=(8,6))
# data['workclass'].hist()
# plt.tight_layout()
# plt.show()

# How many persons having bachelor or masters?
print(data['education'].unique())
print(data[(data['education'] == "Masters") | (data['education'] == "Bachelors")])

# alternative
print(data[data['education'].isin(['Bachelors', 'Masters'])])


# Bivariate analysis