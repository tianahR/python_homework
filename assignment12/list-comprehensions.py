# Task 3 : Task 3: List Comprehensions Practice

# Task 3:1 Add code that reads the contents of ../csv/employees.csv into a DataFrame.

import pandas as pd

df = pd.read_csv("../csv/employees.csv")
# print(df.head())

# Task 3:2 Using a list comprehension, create a list of the employee names, first_name + space + last_name.
# The list comprehension should iterate through the rows of the DataFrame. Print the resulting list.
# Hint: If df is your dataframe, df.iterrows() gives an iterable list of rows. 
# Each row is a tuple, where the first element of the tuple is the index,
# and the second element is a dict with the key/value pairs from the row

employee_names = [row[1]["first_name"] + " " + row[1]["last_name"] for row in df.iterrows()]
print("Full name of employees \n", employee_names)

# Task 3.2 Using a list comprehension, create another list from the previous list of names. 
# This list should include only those names that contain the letter "e". Print this list.

names_with_e =  [name for name in employee_names if "e" in name]
print("Name of employees with e in it \n",names_with_e)