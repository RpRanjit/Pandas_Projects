import pandas as pd

data = pd.read_csv("train.csv")
# print(data)

# 1. Display Top 5 Rows of The Dataset
print(data.head())


# 2. Check the Last 3 Rows of The Dataset
print(data.tail(3))


# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
shapes = data.shape
print(f"Number of rows: {shapes[0]}")
print(f"Number of columns: {shapes[1]}")


# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info())

# 5. Get Overall Statistics About The Dataframe
print(data.describe())
print(data.describe(include='all'))

# 6. Data Filtering
print(data.columns)
print(data['Name'])
print(data[['Name', 'Age']])

# for male in the dataset
print(data['Sex'] == "male")
# total
print(sum(data['Sex'] == "male"))

print(data[data['Sex'] == "male"])

# to check the survival
print(data.columns)
print(data['Survived'] == 1)
# total person survived
print(sum(data['Survived'] == 1))
print(data[data['Survived'] == 1])

# 7.Check Null Values In The Dataset
print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data.isnull())
# plt.show()

# /let find out the percentage of missing vlaues
perc_missing_value = data.isnull().sum() *100/(len(data))
print(perc_missing_value)


# 8. Drop the Column
# as we see Cabin column has 77% missing so deop it
data = data.drop('Cabin', axis=1)
# print(data)
print(data.isnull().sum())

# 9. Handle Missing Values
# lets first handle missing values in embarked column
print(data.columns)
print(data['Embarked'].unique())
# we will use mode here because it gives the most frequent occuring value
print(data['Embarked'].mode())
# filling nan by this value

data['Embarked'] = data['Embarked'].fillna('S')
print(data['Embarked'].isnull().sum())

# for age lets fill with average/mean value
data['Age'] = data['Age'].fillna(data['Age'].mean())
print(data.isnull().sum())
# print(data.info())

# 10. Categorical Data Encoding
# if we are doing machile learning then they only understand mathematical value  so we do catagorical data encoding

print(data)
# for sex

print(data['Sex'].unique())
# This will ad Gender into last column
# data['Gender'] = data['Sex'].map({'male':1, 'female': 0})
# what if we want it to come after Sex for that
gender = data['Sex'].map({'male':1, 'female': 0})
data.insert(5, "Gender_New", gender)
print(data)