import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# lets say tere is date time and you want it object as date and tyme use parse_date=['']
data = pd.read_csv("udemy_courses.csv", parse_dates=['published_timestamp'])

print(data.columns)
print(data.dtypes)
# 1. Display Top 10 Rows of The Dataset
print(data.head(10))

# 2. Check Last 5 Rows of The Dataset
print(data.tail())
# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
shapes = data.shape
print("No of rows: ", shapes[0])
print("No of rows: ", shapes[1])

# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info())

# 5. Check Null Values In The Dataset

print(data.isnull().sum())
sns.heatmap(data.isnull())
# plt.show()
# 6. Check For Duplicate Data and Drop Them

print(data.duplicated())
print(data.duplicated().sum())
data = data.drop_duplicates()
print(data.duplicated().sum())
# 7. Find Out Number of Courses Per Subjects
print(data.columns)
print(data['subject'].value_counts())
sns.countplot(data["subject"])
# plt.show()

# 8. For Which Levels, Udemy Courses Providing The Courses
print(data.head(1))
print(data['level'].value_counts())

sns.countplot(data["level"], palette='Set1')
# plt.tight_layout()
# plt.show()


# 9. Display The Count of Paid and Free Courses 
print(data.columns)
print(data['is_paid'].value_counts())

# 10. Which Course Has More Lectures (Free or Paid)?
print(data.groupby('is_paid')['num_lectures'].mean())
# 11. Which Courses Have A Higher Number of Subscribers Free or Paid?
print(data.groupby('is_paid')['num_subscribers'].sum())

# 12. Which Level Has The Highest Number of Subscribers?
print(data.groupby('level')['num_subscribers'].sum())
# use box-plot to analyse it

# 13. Find Most Popular Course Title

print(data.columns)
print(data[data['num_subscribers'].max() == data['num_subscribers']])
# 14. Display 10 Most Popular Courses As Per Number of Subscribers
# 15. Find The Course Which Is Having The Highest Number of Reviews.
# 16. Does Price Affect the Number of Reviews?
# 17. Find Total Number of Courses Related To Python
# 18. Display 10 Most Popular Python Courses As Per Number of Subscribers
# 19. In Which Year The Highest Number of Courses Were Posted?
# 20. Display Category-Wise Count of Posted Subjects [Year Wise] 