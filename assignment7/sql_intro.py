import sqlite3



# Task 3: Populate Tables with Data

# Create functions, one for each of the tables, to add entries. 
# Include code to handle exceptions as needed, and to ensure that there is no duplication of information.
# The subscribers name and address columns don't have unique values -- you might have several subscribers with the same name -- 
# but when creating a subscriber you should check that you don't already have an entry where BOTH the name and the address are
# the same as for the one you are trying to create.

def add_publisher(cursor,name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?);", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")
        
        
def add_magazine(cursor,name,publisher):
    cursor.execute("SELECT * FROM publishers WHERE name = ?", (publisher,)) 
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    else:
        print(f"There was no publisher named {publisher}.")
        return
    
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?);", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")
        
        
def add_subscriber(cursor,name,address):
    cursor.execute("SELECT * from subscribers WHERE name = ? AND address = ?;",(name,address))
    results = cursor.fetchall()
    if len(results) > 0:
        print("That subscriber is already in the database")
        return
    else:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?);", (name, address))
        
        
def add_subscription(cursor,name,address,magazine,expiration_date):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name,address)) 
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print("That subscriber is not in the database.")
        return
    
    cursor.execute("SELECT * FROM magazines WHERE name = ?", (magazine,)) 
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There was no magazine named {magazine}.")
        return
    
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?;", (subscriber_id,magazine_id))    
    results = cursor.fetchall()
    if len(results) > 0:
        print("That subscription was already in the database.")
        return
    else:
        cursor.execute("INSERT INTO subscriptions (subscriber_id,magazine_id,expiration_date) VALUES (?, ?, ?);", 
                   (subscriber_id, magazine_id,expiration_date))

        
    
    
    
        

# Task 1: Create a New SQLite Database
# Connect to the database
try:
    
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        
    
        
# Task 2: Define Database Structure

# 
# We have publishers that publish magazines.  
# Each publisher has a unique name, and so does each magazine.  
# There is a one-to-many relationship between publishers and magazines.  
# We also have subscribers, and each subscriber has a name and an address.  
# We have a many-to-many association between subscribers and magazines, 
# because a subscriber may subscribe to several magazines, and a magazine may have many subscribers.  
# So, we have a join table called subscriptions.  The subscriptions table also stores the expiration_date 
# (a string) for the subscription.  All the names, the address, and the expiration_date must be non-null.
# 

# Task 2:1 Think for a minute.
  
# There is a one-to-many relationship between publishers and magazines.  
# Which table has a foreign key? Where does the foreign key point? 
# ANSWER : The table magazines has the foreign-key. The foreign key point to the publisher id

# How about the subscriptions table: What foreign keys does it have?
# ANSWER : The subscriptions table has 2 foreign keys, which point to the subscriber id and magazines id

# Task 2:2 Add SQL statements to sql_intro.py that create the following tables:publishers, magazines,subscribers,subscriptions

        cursor = conn.cursor()

        # Create table publishers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)
        
        # create table magazines
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)  
        )
        """)
        
        # create table subscribers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL  
        )
        """)
        
        # create table subscriptions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions(
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)
        
        print("Tables created successfully.")
        
        
        # Task 3:3 Populate each of the 4 tables with at least 3 entries. 
        # Insert sample data into tables

        add_publisher(cursor, 'Time USA')
        add_publisher(cursor,'Conde Nast')  
        add_publisher(cursor,'Springer Nature')
        
        add_magazine(cursor,'Time', 'Time USA')
        add_magazine(cursor,'Vogue', 'Conde Nast')
        add_magazine(cursor,'Scientific American', 'Springer Nature')
        
        add_subscriber(cursor,'Fara','2184 Northlake Heights')
        add_subscriber(cursor,'Tsiry','PO BOX 400')
        add_subscriber(cursor,'Mihatia','3145 Queens Walk')
        
        add_subscription(cursor,'Fara','2184 Northlake Heights','Time','2027-12-13')
        add_subscription(cursor,'Tsiry','PO BOX 400','Vogue','2027-12-13')
        add_subscription(cursor,'Mihatia','3145 Queens Walk','Scientific American','2027-12-13')
        
        
        print("Sample data inserted successfully.")
        
        conn.commit() 
        
        

        # Task 4: Write SQL Queries
        
        # Task 4:1 Write a query to retrieve all information from the subscribers table.
        
        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        print('\n Subscribers :')
        for row in result:
            print(row)
            
        # Task 4:2 Write a query to retrieve all magazines sorted by name.
        
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        result = cursor.fetchall()
        print(" \n Magazines sorted by name :")
        for row in result:
            print(row)
            
        # Task 4:3 Write a query to find magazines for a particular publisher, 
        # one of the publishers you created. This requires a JOIN.
        
        cursor.execute("""SELECT * FROM magazines m JOIN publishers p ON p.publisher_id = m.publisher_id 
                       WHERE p.name = 'Time USA'""")
        result = cursor.fetchall()
        print("\n Magazines and publishers")
        for row in result:
            print(row)
            

except sqlite3.Error as e:
    print(f"An error occurred: {e}")