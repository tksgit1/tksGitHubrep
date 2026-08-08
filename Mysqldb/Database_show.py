import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="college"
)

cursor = conn.cursor()
query = "SELECT * FROM Student"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
