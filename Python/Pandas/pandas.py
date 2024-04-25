# create a dataframe from a dictionary and display it.

import pandas as pd 

dict = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 35, 30, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

index_labels = ['A','B','C','D']

df = pd.DataFrame(dict, index_labels)
print(df)

print("Information is: ")
print(df.info())

selected_columns = df[['Name', 'City']]
print("Selected columns are:\n",selected_columns)

mean_age = df['Age'].mean()
print("Mean age is: ", mean_age)

aged = df[df['Age'] > 30]
print("People with age>30 are:\n", aged)