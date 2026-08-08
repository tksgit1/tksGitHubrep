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

# delete statement for tblemployee
# which deletes employee Aishwarya having empid 3
employeetbl_delete = "DELETE FROM tblemployee WHERE empid=3"

# execute the delete statement and commit to the database
c.execute(employeetbl_delete)
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
