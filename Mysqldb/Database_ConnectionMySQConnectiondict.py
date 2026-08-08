from mysql.connector import connection

dict = {
  'user': 'root',
  'host': 'localhost',
  'database': 'testdb1',
  'password': 'Test@135mac',
  'raise_on_warnings': True
}
# Connecting to the server
conn = connection.MySQLConnection(**dict)

print(conn)
print("\n Database connected")

cursor = conn.cursor()
query = "SELECT * FROM tblemployee"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# Disconnecting from the server
conn.close()

