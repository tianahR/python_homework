import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task2

# Create a function called read_employees that has no arguments, and do the following within it.
# Declare an empty dict. You'll add the key/value pairs to that. Declare also an empty list to store the rows.
# You next read a csv file. Use a try block and a with statement, so that your code is robust and so that the file gets closed.
# Read ../csv/employees.csv using csv.reader(). (This csv file is used in a later lesson to populate a database.)
# As you loop through the rows, store the first row in the dict using the key "fields". These are the column headers.
# Add all the other rows (not the first) to your rows list.
# Add the list of rows (this is a list of lists) to the dict, using the key "rows".
# The function should return the dict.
# Add a line below the function that calls read_employees and stores the returned value in a global variable called employees. 
# Then print out this value, to verify that the function works.
# In this case, it's not clear what to do if you get an exception. 
# You might get an exception because the filename is bad, or because the file couldn't be parsed as a CSV file. 
# For now, just use the same approach as described above: catch the exception, print out the information, and exit the program. 
# One likely exception in this case is an error in the syntax of your code

def read_employees():
    employees = {} #dict
    rows = [] #list
    
    try:
        
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    employees["fields"] = row
                    first=False
                else: 
                    rows.append(row)
            employees["rows"] = rows
        return employees
            
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
employees = read_employees()
print("employees: ", employees)


# Task 3 Find the column index
# Create a function called column_index. The input is a string. 
# The function looks in employees["fields"] (an array of column headers) to find the index of the column header requested.

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column=column_index("employee_id")

print(column_index("first_name"))
print(column_index("last_name"))
print(column_index("phone"))
print(employee_id_column)


# Task 4: Find the Employee First Name
# Create a function called first_name.  It takes one argument, the row number.  The function should retrieve the value of first_name from a row as stored in the employees dict.
# You should first call your column_index function to find out what column index you want.
# Then you go to the requested row as stored in the employees dict, and get the value at that index in the row.
# Return the value.

def first_name(row_number):

    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]
    
print(first_name(3))


# Task 5: Find the Employee: a Function in a Function
# Create a function called employee_find.  This is passed one argument, an integer.  Just call it employee_id in your function declaration. We want it to return the rows with the matching employee_id.  There should only be one, but sometimes a CSV file has bad data.
# We could do this with a loop.  But we are going to use the filter() function. 
# Inside the employee_find function (yes, you do declare functions inside functions sometimes), 
# create the following employee_match function:

# def employee_match(row):
#    return int(row[employee_id_column]) == employee_id

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

print(employee_find(4))


# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print(employee_find(4))

# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key = lambda row : row[last_name_index])
    return employees["rows"]

sort_by_last_name()
print("After sort: ", employees)


# Task 8: Create a dict for an Employee
# Create a function called employee_dict.  It is passed a row from the employees dict (not a row number).  It returns a dict.

# The keys in the dict are the column headers from employees["fields"].
# The values in the dict are the corresponding values from the row.
# Do not include the employee_id in the dict. You skip that field for now.
# Return the resulting dict for the employee.


def employee_dict(row):
    return_dict = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            return_dict[field] = row[i]
    return return_dict

print("employee_dict: ", employee_dict(employees["rows"][19]))


# def employee_dict_2(row):
#     return {field: value for field, value in zip(employees["fields"], row) if field != "employee_id"}

# print("employee_dict: ", employee_dict_2(employees["rows"][19]))


# Task 9: A dict of dicts, for All Employees
# Create a function called all_employees_dict.

# The keys in the dict are the employee_id values from the rows in the employees dict.
# For each key, the value is the employee dict created for that row. (Use the employee_dict function you created in task 8.)
# The function should return the resulting dict of dicts.

def all_employees_dict():
    return_dict = {}
    for row in employees["rows"]:
        return_dict[row[employee_id_column]]=employee_dict(row)
    return return_dict

print("all_employees_dict: ", all_employees_dict())


# Task 10: Use the os Module
# Within the terminal, enter the command export THISVALUE=ABC.
# Add a line to assignment2.py to import the os module.
# Create a function get_this_value().  This function takes no parameters 
# and returns the value of the environment variable THISVALUE.

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

# Task 11: Creating Your Own Module
# In the same folder, create a file called custom_module.py, with the following contents:
# secret = "shazam!"

# def set_secret(new_secret):
#   global secret
#    secret = new_secret
# Add the line import custom_module to assignment2.py.

# Create a function called set_that_secret.  It should accept one parameter, 
# which is the new secret to be set.  It should call custom_module.set_secret(), 
# passing the parameter, so as to set the secret in custom_module.

# Add a line to your program to call set_that_secret, passing the new string of your choice.

# In another line, print out custom_module.secret.  Verify that it has the value you expect.

def set_that_secret(secret):
    custom_module.set_secret(secret)
    
set_that_secret("Fara")

print(custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv

# Create a function called read_minutes.  It takes no parameters. 
# It creates two dicts, minutes1 and minutes2, by reading ../csv/minutes1.csv and ../csv/minutes2.csv.  
# Each dict has fields and rows, just as the employees dict had. 
# However! As you create the list of rows for both minutes1 and minutes2, convert each row to a tuple. 
# The function should return both minutes1 and minutes2.  
# Note You can return several values from a Python function, as follows: return v1, v2.  
# Don't worry about duplicates yet.  They will be dealt with in later tasks.  Think about the DRY 
# (Don't repeat Yourself principal).  You may want to create a helper function to avoid duplicating code.

# function to read minutes to avoid duplicate code :read_minutes_data(data)
# where data is the file to read
def read_minutes_data(data):
    minutes_data = {} #dict
    rows = [] #list
    
    try:
        
        with open(data, "r", newline="") as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    minutes_data["fields"] = row
                    first=False
                else: 
                    rows.append(tuple(row))
            minutes_data["rows"] = rows
        return minutes_data 
            
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
        
minutes1_data = read_minutes_data("../csv/minutes1.csv")
minutes2_data = read_minutes_data("../csv/minutes2.csv")



def read_minutes():
    return minutes1_data,minutes2_data

# Call the function within your assignment2.py script.  
# Store the values from the values it returns in the global variables minutes1 and minutes2. 
# Note When a function returns several values, you get them as follows: v1, v2 = function().
# Print out those dicts, so that you can see what's stored.

minutes1, minutes2 = read_minutes() #global variable minutes1, minutes2

print("Minutes 1 \n",minutes1)
print ("=======================================\n")

print("Minutes 2 \n",minutes2)
print ("=======================================\n")



# Task 13: Create minutes_set
# Create a function called create_minutes_set.  It takes no parameters. 
# It creates two sets from the rows of minutes1 and minutes2 dicts.  
# (This is just type conversion.  However, to make it work, each row has to be hashable!  
# Sets only support hashable elements.  Lists aren't hashable, so that is why you stored the rows as tuples in Task 12.)  
# Combine the members of both sets into one single set.  (This operation is called a union.)  
# The function returns the resulting set.

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    
    set_union = set1.union(set2)
    return set_union

minutes_set = create_minutes_set()

print ("=======================================\n")
print ("=========MINUTES SET===============\n")
print(minutes_set)



# Task 14: Convert to datetime
# create_minutes_list()

# Create a function called create_minutes_list.  It takes no parameters, and does the following:

# Create a list from the minutes_set. This is just type conversion.
# Use the map() function to convert each element of the list. At present, 
# each element is a list of strings, where the first element of that list is the name of the recorder and 
# the second element is the date when they recorded.
# The map() should convert each of these into a tuple. 
# The first element of the tuple is the name (unchanged). 
# The second element of the tuple is the date string converted to a datetime object.
# You convert the date strings into datetime objects using datetime.strptime(string, "%B %d, %Y").
# So, you could use the following lambda: lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))
# The function should return the resulting list.

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list_convert = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list_convert

minutes_list = create_minutes_list()

print ("=======================================\n")
print ("=========MINUTES LIST ===============\n")
print(minutes_list)



# Task 15: Write Out Sorted List

# Create a function called write_sorted_list.  It takes no parameters.  It should do the following:

# Sort minutes_list in ascending order of datetime.
# Call map again to convert the list. In this case, for each tuple, you create a new tuple. 
# The first element of the tuple is the name (unchanged). 
# The second element of the tuple is the datetime converted back to a string, using datetime.strftime(date, "%B %d, %Y")
# Open a file called ./minutes.csv. Use a csv.writer to write out the resulting sorted data. 
# The first row you write should be the value of fields the from minutes1 dict. The subsequent rows should be the elements 
# from minutes_list.
# The function should return the converted list.

def write_sorted_list():
    
    minutes_list.sort(key=lambda x:x[1]) #sort by datetime
    minutes_list_convert = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)) 
    
    with open("./minutes.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        
        for row in minutes_list_convert:
            writer.writerow(row)
    
    
    return minutes_list_convert


print ("=======================================\n")
print ("=========MINUTES LIST SORTED===============\n")

print(write_sorted_list())
    




    
    


    
