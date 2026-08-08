# Python implementation to update data of a table in MySQL
import mysql.connector

# connecting to the mysql server

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Test@135mac",
    database="testdb1"
)

# cursor object c
c = db.cursor()

# update statement for tblemployee
# which modifies the salary of Vani
employeetbl_update = "UPDATE tblemployee \
SET salary = 115000 WHERE empid = 1"

# execute the update query to modify
# the salary of employee with
# employee id = 1 and commit to the database
c.execute(employeetbl_update)
db.commit()

# cursor object c
c = db.cursor()

# select statement for tblemployee which returns all columns
employeetbl_select = """SELECT * FROM tblemployee"""

# execute the select query to fetch all rows
c.execute(employeetbl_select)

# fetch all the data returned by the database
employee_data = c.fetchall()

# print all the data returned by the database
for e in employee_data:
    print(e)

# finally closing the database connection
db.close()
