# Task 1: Plotting with Pandas

# Create a file called employee_results.py.
# Load a DataFrame called employee_results using SQL. 
# You connect to the ../db/lesson.db database. You use SQL to join the employees table with the orders 
# table with the line_items table with the products table. You then group by employee_id, 
# and you SELECT the last_name and revenue, where revenue is the sum of price * quantity. 
# Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
# Give appropriate titles, labels, and colors.
# Show the plot.

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    
    sql_statement = """SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e JOIN Orders o ON e.employee_id = o.employee_id JOIN line_items l 
    ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;"""
    
    df = pd.read_sql_query(sql_statement, conn)

df.plot(x="last_name", y="revenue", kind="bar", color="skyblue", title="Employee Results")
plt.show()