

# Task 2: A Line Plot with Pandas
# Create a file called cumulative.py. The boss wants to see how money is rolling in.
# You use SQL to access ../db/lesson.db again. You create a DataFrame with the order_id and the total_price for each order. 
# This requires joining several tables, GROUP BY, SUM, etc.
# Add a "cumulative" column to the DataFrame. This is an interesting use of apply():
# def cumulative(row):
#    totals_above = df['total_price'][0:row.name+1]
#    return totals_above.sum()

# df['cumulative'] = df.apply(cumulative, axis=1)
# Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.
# Show the Plot.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT o.order_id, SUM(price * quantity) AS total_price 
    FROM orders o JOIN line_items l 
    ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY o.order_id;"""
    df = pd.read_sql_query(sql_statement, conn)

def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(x="order_id", y="cumulative", kind="line", title="Cumulative Revenue")
plt.show()