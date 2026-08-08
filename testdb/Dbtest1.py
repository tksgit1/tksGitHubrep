import mysql.connector as SQLC


def CreateTable():
    # Connect to the College database
    DataBase = SQLC.connect(
        host="localhost",  # Server name
        user="root",       # MySQL username
        password="Test@135mac",  # MySQL password
        database="College"  # Database name
    )



    # Create a cursor object
    Cursor = DataBase.cursor()


    # SQL query to create the table
    #TableName = """CREATE TABLE Student2 (
    #                Name VARCHAR(255),
    #                Roll_no INT
    #              );"""

    # Execute the query to create the table
 #   Cursor.execute(myuser)
    print("Student Table is Created in the Database")



    # SQL query to create new user
    Myuser = """ CREATE USER 'gfguser1'@'localhost' IDENTIFIED BY 'abcd'"""

  Cursor.execute(Myuser)

# Calling the CreateTable function
CreateTable()