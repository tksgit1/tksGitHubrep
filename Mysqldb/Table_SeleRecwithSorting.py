import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test@135mac",
    database="testdb1"
)

cursor = conn.cursor()
query = "SELECT empName, salary FROM tblemployee ORDER BY salary DESC"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
