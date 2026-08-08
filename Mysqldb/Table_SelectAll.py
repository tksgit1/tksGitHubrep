import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test@135mac",
    database="Testdb1"
)

cursor = conn.cursor()
query = "SELECT * FROM tblemployee"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
