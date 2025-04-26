# Task 6: Read Data into a DataFrame

# We want to find out how many times each product has been ordered, and what was the total price paid by product.

# Task 6:2 Read data into a DataFrame, as described in the lesson. 
# The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a 
# JOIN of the line_items table and the product table. 
# Hint: Your ON statement would be ON line_items.product_id = products.product_id.

import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    
    sql_statement = """
    SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price FROM line_items l JOIN products p 
    ON l.product_id = p.product_id
    """
    
    df = pd.read_sql_query(sql_statement, conn)
    
    # Task 6:3 Print the first 5 lines of the resulting DataFrame
    print("\n",df.head())
    
    # Task 6:4 Add a column to the DataFrame called "total". This is the quantity times the price
    df['total'] = df['quantity'] * df['price']
    print("\n",df.head())
    
    # Task 6:5 Add groupby() code to group by the product_id. Use an agg() method that specifies 'count'
    # for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'. 
    # Print out the first 5 lines of the resulting DataFrame
    
    df = df.groupby('product_id').agg({'line_item_id':'count','total': 'sum', 'product_name': 'first'})
    print("\n",df.head())
    
    # Task 6:6 Sort the DataFrame by the product_name column.
    df = df.sort_values(by='product_name')
    print("\n",df.head())
    
    # Task 6:7 Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory.
    df.to_csv("./order_summary.csv")
    