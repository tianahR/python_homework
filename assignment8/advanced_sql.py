import sqlite3

# Task 1: Understanding Subqueries

# Problem Statement:

# For each of the first 5 orders (as ordered by order_id), find the each of the product names for the order. 
# Return a list that includes the order_id, the line_item_id, and the product name.  There are several steps here.  
# You need a subquery to retrieve the order_id for the first 5 orders.  In this subquery, you use ORDER BY order_id and LIMIT 5. 
# In the main query, you need to select the order_id, line_item_id, and product_name from the orders table, the line_items table, 
# and the products table.  Then you need a WHERE clause: WHERE o.order_id IN (...).  
# The subquery is what returns the set of order_ids you want to check.

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")  
        cursor = conn.cursor()
        
        query1 = """
        SELECT o.order_id, l.line_item_id, p.product_name 
        FROM orders o JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON p.product_id = l.product_id
        WHERE o.order_id IN ( SELECT order_id FROM orders ORDER BY order_id LIMIT 5);
        """
        
        cursor.execute(query1)
        
        result = cursor.fetchall()
        print('\n Each Product names in the 5 first orders:')
        
        for row in result:
            print(row)


# TASK 2: Complex JOINs with Aggregation

# Problem Statement:

# Find the total price of each of the first 5 orders.  Again, there are several steps.  
# You need to join the orders table with the line_items table and the products table.  
# You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product price 
# times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery.
# Print out the order_id and the total price for each of the rows returned.

    query2 = """
    SELECT o.order_id, SUM(p.price*l.quantity) FROM orders o 
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p on p.product_id = l.product_id 
    GROUP BY o.order_id 
    ORDER BY o.order_id LIMIT 5;
    """

    cursor.execute(query2)
    
    result = cursor.fetchall()
    print('\n Total price of each of the first 5 orders:')
    
    for row in result:
        print(row)
    
    

except sqlite3.Error as e:
    print(f"An error occurred: {e}")