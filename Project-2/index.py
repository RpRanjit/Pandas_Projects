import pandas as pd

data = pd.read_csv("Salaries.csv")
# print(data)

# Display Top 10 rows of the datasets
# print(data.head(10))

# Check Last 10 rows of the Dataset
# print(data.tail(10))

# Find Shape of our Dataset(Number of rows and Number of Columns)
# print(data.shape)
# print("Number of rows", data.shape[0])
# print("Number of columns:", data.shape[1])

# Getting Information About Our Datasets like Total Number Rows, Total Number of Columns, Datatypes of Each Column and Memory Requirement
# print(data.info())

# Check Null Values in the dataset
# print(data.isnull().sum())

# Drop ID, Notes, Agency, and Status Columns
# print(data.columns)
# data = data.drop(["Id", "Notes", "Agency", "Status"], axis=1)
# print(data)

# Get Overall Statistics About the dataframe
# print(data.describe())

# Find the Occurance of the Employees Names(Top 5)
# print(data.columns)
# print(data["EmployeeName"])
# print(data["EmployeeName"].value_counts())
# print(data["EmployeeName"].value_counts().head())

# Find the number of Unique Job Titles
# print(data.columns)
# print(data["JobTitle"].nunique())

# Total Number of Job Titles Contain Captain
# print(data.columns)
# print(data["JobTitle"])
# filter_data = data[data["JobTitle"].str.contains("Captain", case=True)]
# print(filter_data.count())
# print(filter_data["JobTitle"])

# Display All the Employee Names From Fire Departments
# print(data.columns)
# print(data["JobTitle"])
# filtered_data = data[data["JobTitle"].str.contains("Fire Department", case= False)]
# print(filtered_data["JobTitle"])
# print(filtered_data["EmployeeName"])

# Find Minimum, maximum and average BasePay
# print(data.columns)
# print(data["BasePay"])
# # In BasePay there are string like NAN, Not provide So we will convert them into numeric data
data["BasePay"] = pd.to_numeric(data["BasePay"], errors="coerce")
# print("The Minimum BasePay is", data["BasePay"].min())
# print("The Maximum BasePay is", data["BasePay"].max())
# print("The Average BasePay is", data["BasePay"].mean())

# Replace "Not Provided" in EmployeeName Column to NaN
import numpy as np

# print(data.columns)
# print(data["EmployeeName"])
# print(data["EmployeeName"].replace("Not provided", np.nan))
# # Now to exactly originate into actual data
# data["EmployeeName"] = data["EmployeeName"].replace("Not provided", np.nan)


# Drop The Rows Having 3 Missing Values
# print(data[data.isnull().sum(axis=1) == 4])
# filtered_data = data[data.isnull().sum(axis=1) == 4]
# print(filtered_data)
# print(data.drop(filtered_data.index, axis=0, inplace=True))

# Find the Job Title of Albert Rardini

# print(data.columns)
# print(data["EmployeeName"])
# print(data[data["EmployeeName"] == "ALBERT PARDINI"]["JobTitle"])

#  How Much ALBERT PARDINI make (Include Benefits)
# print(data.columns)
# print(data[data["EmployeeName"] == "ALBERT PARDINI"]["TotalPayBenefits"])

# Display the name of the person having the heighest basepay
# print(data.columns)
# print(data.info())
# result = data[data["BasePay"].max() == data["BasePay"]]
# print(result["EmployeeName"])

# Find the Average Base Pay of all Employee Per Year
print(data.columns)
print(data.groupby("Year")["BasePay"].mean())

# Find Average BasePay od All Employee Per JobTitle
print(data.columns)
print(data.groupby("JobTitle")["BasePay"].mean())

# Find Average BasePay of Employee Having Job Title Accountant
print(data.columns)
print(data[data["JobTitle"] == "ACCOUNTANT"]["BasePay"].mean())

# Find Top 5 Most Common Jobs

print(data.columns)
print(data["JobTitle"].value_counts().head())