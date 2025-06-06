import sqlite3


# TASK 1 : Complex JOINs with Aggregation

# Problem Statement:

# Find the total price of each of the first 5 orders.  Again, there are several steps.  
# You need to join the orders table with the line_items table and the products table.  
# You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product price 
# times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery.
# Print out the order_id and the total price for each of the rows returned.

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")  
        cursor = conn.cursor()

    query1 = """
    SELECT o.order_id, SUM(p.price*l.quantity) FROM orders o 
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p on p.product_id = l.product_id 
    GROUP BY o.order_id 
    ORDER BY o.order_id LIMIT 5;
    """

    cursor.execute(query1)
    
    result = cursor.fetchall()
    print('\n TASK 1 : Total price of each of the first 5 orders:')
    
    for row in result:
        print(row)

# Task 2 : Understanding Subqueries

# Problem Statement:

# For each of the first 5 orders (as ordered by order_id), find the each of the product names for the order. 
# Return a list that includes the order_id, the line_item_id, and the product name.  There are several steps here.  
# You need a subquery to retrieve the order_id for the first 5 orders.  In this subquery, you use ORDER BY order_id and LIMIT 5. 
# In the main query, you need to select the order_id, line_item_id, and product_name from the orders table, the line_items table, 
# and the products table.  Then you need a WHERE clause: WHERE o.order_id IN (...).  
# The subquery is what returns the set of order_ids you want to check.


        
    query2 = """
    SELECT o.order_id, l.line_item_id, p.product_name 
    FROM orders o JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON p.product_id = l.product_id
    WHERE o.order_id IN ( SELECT order_id FROM orders ORDER BY order_id LIMIT 5);
    """
    
    cursor.execute(query2)
    
    result = cursor.fetchall()
    print('\n TASK 2 : Each Product names in the 5 first orders:')
    
    for row in result:
        print(row)
            
            
# Problem Statement:

# For each customer, find the average price of their orders.  
# This can be done with a subquery. You compute the price of each order as in part 1, 
# but you return the customer_id and the total_price.  That's the subquery. 
# You need to return the total price using AS total_price, and you need to return the customer_id with AS customer_id_b, 
# for reasons that will be clear in a moment.  
# In your main statement, you left join the customer table with the results of the subquery,
# using ON customer_id = customer_id_b.  You aliased the customer_id column in the subquery so 
# that the column names wouldn't collide.  Then group by customer_id -- this GROUP BY comes after the subquery -- 
# and get the average of the total price of the customer orders.  Return the customer name and the average_total_price.

    query2 = """
    SELECT customers.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers LEFT JOIN 
    (SELECT orders.customer_id AS customer_id_b, SUM(products.price * line_items.quantity) AS total_price
    FROM orders JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON line_items.product_id = products.product_id GROUP BY orders.order_id
    ) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id;

    """
    
    cursor.execute(query2)
        
    result = cursor.fetchall()
    print('\n TASK 2 : For each customer, the average price of their orders  :')
        
    for row in result:
        print(row)



        
        
# Task 3: An Insert Transaction Based on Data

# Problem Statement:

# You want to create a new order for the customer named Perez and Sons.  
# The employee creating the order is Miranda Harris.  
# The customer wants 10 of each of the 5 least expensive products.  
# You first need to do a SELECT statement to retrieve the customer_id, 
# another to retrieve the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  
# Then, you create the order record and the 5 line_item records comprising the order.  
# You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements.
# You have to use the order_id for the order record you created in the line_items records. 
# The inserts must occur within the scope of one transaction. 
# Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.

    
    # retrieve the customer_id
    query3="""
    SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'
    """
    cursor.execute(query3)
    result = cursor.fetchone()
    customer_id = result[0]
    # print("\n Customer ID ",customer_id)
    
    # retrieve the product_ids of the 5 least expensive products
    query3="""
    SELECT product_id FROM products ORDER BY price DESC LIMIT 5
    """
    cursor.execute(query3)
    result = cursor.fetchall()
    # print("\n Product_ids of the 5 least expensive products ")
    # for row in result:
    #     print(row)
    products = result
        
    # retrieve the employee_id of Miranda Harris
    query3="""
    SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'
    """
    cursor.execute(query3)
    result = cursor.fetchone()
    employee_id = result[0]
    # print("\n Employee ID ",employee_id)
    
    # create the order record 
    query3="""
    INSERT INTO orders (customer_id,employee_id,date) VALUES (?,?,DATETIME('now')) RETURNING order_id
    """
    cursor.execute(query3,(customer_id,employee_id))
    result = cursor.fetchone()
    # print("\n Order ",result)
    order_id = result[0]
    
    
    # create the 5 line_item records comprising the order. 
    for i in range(5):       
        query3="""INSERT INTO line_items (order_id,product_id, quantity) VALUES (?,?,?) """
        cursor.execute(query3,(order_id,products[i][0],10))
    conn.commit()
    
    # print out the list of line_item_ids for the order along with the quantity and product name for each.

    
    query3="""SELECT l.line_item_id, l.quantity, p.product_name FROM line_items l JOIN products p ON 
        l.product_id = p.product_id WHERE l.order_id = ?;"""
        
    cursor.execute(query3, (order_id,))
    
    result = cursor.fetchall()
    print("\n TASK 3 : List of line_item_ids for the order along with the quantity and product name for each. ")
    for row in result:
        print(row)
        
        
# Task 4: Aggregation with HAVING
    
# Problem Statement:

# Find all employees associated with more than 5 orders.  
# You want the first_name, the last_name, and the count of orders.  
# You need to do a JOIN on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.

    query4 = """SELECT first_name, last_name, COUNT(order_id) FROM employees e JOIN orders o 
        ON e.employee_id = o.employee_id 
        GROUP BY e.employee_id 
        HAVING COUNT(order_id) >5;"""
        
    cursor.execute(query4)
    result = cursor.fetchall()
    
    print("\n TASK 4 : All employees associated with more than 5 orders. ")
    
    for row in result:
        print(row)
    
    
        
except sqlite3.Error as e:
    print(f"An error occurred: {e}")