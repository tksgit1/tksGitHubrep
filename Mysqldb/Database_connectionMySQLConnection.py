from mysql.connector import connection

# Connecting to the server
conn = connection.MySQLConnection(user = 'root',
                            passwd = 'Test@135mac',
                            host = 'localhost',
                            database = 'testdb1')

print(conn)
print("\n Database connected")

cursor = conn.cursor()
query = "SELECT empid, empname FROM tblemployee"
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# Disconnecting from the server
conn.close()