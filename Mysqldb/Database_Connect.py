import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(user = 'root',
                               password = 'Test@135mac',
                               host = 'localhost',
                              database = 'testdb1')
print(conn)
print("\n Database connected")

cursor = conn.cursor()
query = "SELECT * FROM tblemployee"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# Disconnecting from the server
conn.close()

