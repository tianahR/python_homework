# import numpy as np
import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
#Task1.1 Create a DataFrame from a dictionary:

# Use a dictionary containing the following data:
# Name: ['Alice', 'Bob', 'Charlie']
# Age: [25, 30, 35]
# City: ['New York', 'Los Angeles', 'Chicago']
# Convert the dictionary into a DataFrame using Pandas.
# Print the DataFrame to verify its creation.
# save the DataFrame in a variable called task1_data_frame and run the tests.


def task1_data_frame():
    data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']
        }
    return pd.DataFrame(data)
    
    
task1_data_frame = task1_data_frame()


print("\n========INITIAL DATAFRAME WITHOUT SALARY===============")
print(task1_data_frame)


# Task1.2 Add a new column:

# Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
# Add a column called Salary with values [70000, 80000, 90000].
# Print the new DataFrame and run the tests.

def added_column():
    df = task1_data_frame.copy()
    salary = [70000, 80000, 90000]
    df["Salary"] = salary
    
    return df
    

task1_with_salary = added_column()

print("\n========ADDED COLUMN SALARY =============")
print(task1_with_salary)


# Task 1:3 Modify an existing column:

# Make a copy of task1_with_salary in a variable named task1_older
# Increment the Age column by 1 for each entry.
# Print the modified DataFrame to verify the changes and run the tests.

def increment_column():
    task1_older = task1_with_salary.copy()
    task1_older["Age"]= task1_older["Age"].add(1)
    return task1_older

task1_older = increment_column()

print("\n=========INCREMENT AGE ==============")
print(task1_older)


# Task 1:4 Save the DataFrame as a CSV file:

# Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
# Look at the contents of the CSV file to see how it's formatted.
# Run the tests.

def write_csv():
    task1_older.to_csv("employees.csv", index=False)
    
write_csv()

# ========================================================
# Task 2: Loading Data from CSV and JSON

# task 2:1 Read data from a CSV file:

# Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
# Print it and run the tests to verify the contents.

def read_data_frame_from_csv():
    df = pd.read_csv('employees.csv')
    return df

task2_employees = read_data_frame_from_csv()

print("\n==============DATAFRAME FROM EMPLOYEES.CSV===============")
print(task2_employees)


# Task 2.2 Read data from a JSON file:

# Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, 
# and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
# Load this JSON file into a new DataFrame and assign it to the variable json_employees.
# Print the DataFrame to verify it loaded correctly and run the tests.


def create_json_file():
    data = {
            'Name': ['Eve', 'Frank'],
            'Age': [28, 40],
            'City': ['Miami', 'Seattle'],
            'Salary':[60000,95000]
        }
    df = pd.DataFrame(data)
    df.to_json("additional_employees.json")

create_json_file()
    

def read_data_frame_from_json():
    df = pd.read_json('additional_employees.json')
    return df

json_employees = read_data_frame_from_json()
print("\n==============DATAFRAME FROM additional_employees.json===============")
print(json_employees)


# Task 2.3 Combine DataFrames:

# Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees.
# Print the combined Dataframe and run the tests.

def concat_json_employees():
    #  combined_df = pd.concat([data, more_data], ignore_index=True)
    df = pd.concat([task2_employees,json_employees],ignore_index=True)
    return df 


more_employees = concat_json_employees()
print("\n==============DATAFRAME concatenation of task2-employees and json_employees===============")
print(more_employees)


# ====================================================================
# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Task 3.1 Use the head() method:

# Assign the first three rows of the more_employees DataFrame to the variable first_three
# Print the variable and run the tests.

def head():
    return more_employees.head(3)
    

first_three = head()
print("\n==============first 3 employees===============")
print(first_three)


# Task 3.2 Use the tail() method:

# Assign the last two rows of the more_employees DataFrame to the variable last_two
# Print the variable and run the tests.

def tail():
    return more_employees.tail(2)

last_two = tail()
print("\n==============last 2 employees===============")
print(last_two)


# Task 3.3 Get the shape of a DataFrame
# Assign the shape of the more_employees DataFrame to the variable employee_shape
# Print the variable and run the tests
# shape returns how many rows, and how many columns

def shape():
    return more_employees.shape #.shape returns how many rows, and how many columns

employee_shape = shape()
print("\n==============employee shape===============")
print(employee_shape)


# Task 3.4 Use the info() method:
# Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.


def info():
    return more_employees.info()

print("\n==============employee info===============")
info()



# =======================================================================================

# Task 4: Data Cleaning

# Task 4.1 Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.

# Print it and run the tests.
# Create a copy of the dirty data in the varialble clean_data (use the copy() method). 
# You will use data cleaning methods to update clean_data.

def dirty_data_read():
    df = pd.read_csv("dirty_data.csv")
    return df

dirty_data = dirty_data_read()
print("\n==============dirty data===============")
print(dirty_data)


clean_data = dirty_data.copy()

print("\n==============clean data===============")
print(clean_data)


# Task 4.2 Remove any duplicate rows from the DataFrame
# Print it and run the tests.

def no_duplicate_rows():
    df = clean_data.drop_duplicates()
    return df 
    

clean_data = no_duplicate_rows()

print("\n==============clean data no duplicate ===============")
print(clean_data)


# Task 4.3 Convert Age to numeric and handle missing values

# Print it and run the tests.

def age_numeric():
    clean_data["Age"] = pd.to_numeric(clean_data["Age"],errors="coerce")
    # mean = clean_data["Age"].mean() #ignoring NAN 
    # clean_data["Age"] = clean_data["Age"].fillna(mean)
    return clean_data

clean_data = age_numeric()
print("\n==============Age to Numeric ===============")
print(clean_data)


# Task 4.4 Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN

# print it and run the tests.

def salary_numeric():
     clean_data["Salary"] = pd.to_numeric(clean_data["Salary"],errors="coerce")
     return clean_data
 
clean_data = salary_numeric()
print("\n==============salary to Numeric ===============")
print(clean_data)


# Task 4.5 Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median

# Print it and run the tests 

def no_missing_age_salary():
    mean = clean_data["Age"].mean() #ignoring NAN 
    clean_data["Age"] = clean_data["Age"].fillna(mean)
    
    median = clean_data["Salary"].median() 
    clean_data["Salary"] = clean_data["Salary"].fillna(median)
    
    return clean_data

clean_data = no_missing_age_salary()
print("\n==============No missing age and no missing salary ===============")
print(clean_data)

def loop_hire_date():

    for date in clean_data["Hire Date"]:
        clean_data["Hire Date"] = clean_data["Hire Date"].str.strip()
        print(date)

loop_hire_date()



# Task 4.6 Convert Hire Date to datetime

# Print it and run the tests

def hire_date_datetime():
    
    clean_data["Hire Date"] = clean_data["Hire Date"].str.strip()
    clean_data["Hire Date"] = clean_data["Hire Date"].apply(lambda x: pd.to_datetime(x, errors="coerce", format="%Y/%m/%d") 
                                       if "/" in str(x) else pd.to_datetime(x, errors="coerce", format="%Y-%m-%d"))
    return clean_data

clean_data = hire_date_datetime()
print("\n==============hire date to datetime ===============")
print(clean_data)


# Task 4.7 Strip extra whitespace and standardize Name and Department as uppercase

# Print it and run the tests

def name_uppercase():
     clean_data["Name"] = clean_data["Name"].str.strip()
     clean_data["Name"] = clean_data["Name"].str.upper()
     return clean_data
 
clean_data = name_uppercase()
print("\n=============NAME UPPERCASE===============")
print(clean_data)


def department_uppercase():
     clean_data["Department"] = clean_data["Department"].str.strip()
     clean_data["Department"] = clean_data["Department"].str.upper()
     return clean_data
 
clean_data = department_uppercase()
print("\n=============Department UPPERCASE===============")
print(clean_data)
    



    

        










    




