# Python code to demonstrate table creation and
# insertions with SQL

# importing module
#import mysql.connector
#import mysql.connector as SQLC
'''
import mysql.connector


print("4")
# Connect to the database server
db_connection = mysql.connector.connect(
    host="localhost",  # Server name
    user="root",       # MySQL username
    password="Test@135mac",  # MySQL password
    database="College"  # Database name
    )

print("3")
# Create a cursor object to execute queries
cursor = db_connection.cursor()
# connecting to the database
print("2")
#connection = SQLC.connect("tksmysqldb")
#cursor = SQLC.connect("tksmysqldb.db")
#sqliteConnection = sqlite3.connect('gfg.db')

def CreateTable():
    print("3")
    # Connect to the College database
    DataBase = SQLC.connect(
        host="localhost",  # Server name
        user="root",       # MySQL username
        password="Test@135mac",  # MySQL password
        database="College"  # Database name
    )


print("1")
# cursor
#crsr = connection.cursor()

# SQL command to insert the data in the table
#sql_command = "USE db_connection;"
#cursor.execute(sql_command)
sql_query = "SHOW DATABASES;"
user_data = ("root", "john@example.com")


#cursor = currentConnection.cursor()
cursor.execute(sql_query, user_data)
db_connection.commit()  # Required for INSERT, UPDATE, and DELETE operations



print(f"Inserted row ID: {cursor.lastrowid}")


print("5")
# another SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates",\
"M", "1980-10-28");"""
cursor.execute(sql_command)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
cursor.commit()

print("6")
# close the connection

cursor.close()
'''

'''
import mysql.connector

print("4")
# Connect to the database server
db_connection = mysql.connector.connect(
    host="localhost",       # Server name
    user="root",            # MySQL username
    password="Test@135mac", # MySQL password
    database="College"      # Database name
)

print("3")
# Create a cursor object to execute queries
cursor = db_connection.cursor()

print("2")
print("1")

# --- FIX 1: Removed the user_data parameter since SHOW DATABASES takes no inputs ---
sql_query = "SHOW DATABASES;"
cursor.execute(sql_query)

# Fetch and print the databases to see if it works
databases = cursor.fetchall()
print("Available Databases:", databases)

print("5")
# SQL command to insert data into the emp table
sql_command = 'INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");'
cursor.execute(sql_command)

# --- FIX 2: Changed cursor.commit() to db_connection.commit() ---
db_connection.commit()

# Print the last inserted ID if the table has an AUTO_INCREMENT primary key
print(f"Inserted row ID: {cursor.lastrowid}")

print("6")
# Close the cursor and connection properly
cursor.close()
db_connection.close()
'''

import mysql.connector

print("4")
# Connect to the database server
db_connection = mysql.connector.connect(
    host="localhost",       # Server name
    user="root",            # MySQL username
    password="Test@135mac", # MySQL password
    database="College"      # Database name
)

print("3")
# Create a cursor object to execute queries
cursor = db_connection.cursor()

print("2")
print("1")

# --- FIX 1: Removed the user_data parameter since SHOW DATABASES takes no inputs ---
sql_query = "SHOW DATABASES;"
cursor.execute(sql_query)

# Fetch and print the databases to see if it works
databases = cursor.fetchall()
print("Available Databases:", databases)

# --- NEW STEP: Create the 'emp' table if it does not exist ---
print("Creating table if missing...")
create_table_query = """
CREATE TABLE IF NOT EXISTS emp (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender CHAR(1),
    birth_date DATE
);
"""
cursor.execute(create_table_query)

print("5")
# SQL command to insert data into the emp table
sql_command = 'INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");'
cursor.execute(sql_command)

# --- FIX 2: Changed cursor.commit() to db_connection.commit() ---
db_connection.commit()

# Print the last inserted ID if the table has an AUTO_INCREMENT primary key
print(f"Inserted row ID: {cursor.lastrowid}")

print("6")
# Close the cursor and connection properly
cursor.close()
db_connection.close()



