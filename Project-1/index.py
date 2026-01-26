import pandas as pd

data = pd.read_csv("ecommerce_purchases.csv")
# print(data)

# Display Top 10 Rows of the Dataset
print(data.head(10))

# Check last 10 rows of the Dataset
print(data.tail(10))

# Check Null Vaalues In the Datasets
print(data.isnull())

# Check the Datatype of Each Column
print(data.dtypes)

# How many Rows and Columns are There In our Dataset?
print(len(data.columns)) # Give no of columns
print(len(data)) # Give no of rows
print(data.info())

# Highest and Lowest Purchase Prices
print(data.columns)
print(data["Purchase Price"])
max_price = data["Purchase Price"].max()
min_price = data["Purchase Price"].min()
print(f"The maximum purchase price is {max_price} and minimum purchase price is {min_price}")

# Average Purchase Price
print(data.columns)
print(data["Purchase Price"])
print("The average Purchaseprice is: ", data["Purchase Price"].mean())


# How  many People Have French 'fr' As Their Langusges?

print(data.columns)
print(data['Language'])

print(len(data[data['Language'] == 'fr']))
# # Alternative method
print(data[data['Language'] == 'fr'].count())

# Job Title Contains Engineer
print(data.columns)
print(data["Job"])

print(len(data[data["Job"].str.contains("engineer")]))
# # Alternative
# # matches “Engineer”, “ENGINEER”, etc. if case = False
Filtered_values = data[data["Job"].str.contains("engineer", case=False)]
print(Filtered_values)

# Find Email of the Person With The following Ip Address: 132.207.160.22

print(data.columns)
print(data["IP Address"])
print(data[data["IP Address"]== "132.207.160.22"])

# How Many People Have Mastercard as their credit card provider and made a purchase above 50
print(data.columns)
print(data[["CC Provider", "Purchase Price"]])
filtered_data = data[(data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50)]

print(filtered_data)

# Find Email of the Person with The following Credit Card Number: 4664825258997302

print(data.columns)
print(data["Credit Card"])
print(data[data["Credit Card"] == 4664825258997302])
print(data[data["Credit Card"] == 4664825258997302]["Email"])

# How Many People Purchase  During The AM and How many People purchase During PM
print(data.columns)
print(data["AM or PM"])
am_purchase_data = data[data["AM or PM"] == "AM"]
pm_purchase_data = data[data["AM or PM"] == "PM"]
print(f"The nu of purchase buring AM is {len(am_purchase_data)} and at PM is {len(pm_purchase_data)}.")

# How Many People Have a credit card that expires in 2020?
print(data.columns)
print(data["CC Exp Date"])
def ExpDate():
    count = 0 
    for date in data["CC Exp Date"]:
        if date.split('/')[1] == '20':
            count += 1
    print(count)

ExpDate()
# Alternatively we can do it by using lambda method
total_people = data[data["CC Exp Date"].apply(lambda x:x[3:] == "20")]
print(len(total_people))

# Top 5 Most Popular Email Provider(e.g. gmail.com, yahoo.com, etc...)
print(data.columns)
print(data["Email"])
list = []
for email in data['Email']:
    list.append(email.split('@')[1])
print(list)
# # Now let's build new column temp
data["Temp"] = list
print(data.columns)
print(data["Temp"])
print(data["Temp"].value_counts())
# for top 5
print(data["Temp"].value_counts().head())

# Alternative method for it
result = data["Email"].apply(lambda x:x.split('@')[1]).value_counts().head()
print(result)
