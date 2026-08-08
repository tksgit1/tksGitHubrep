import mysql.connector

dataBase = mysql.connector.connect(
  host="your-cloud-database-host",  # Replace with your cloud database host
  user="your-username",
  passwd="your-password",
  database="your-database-name"
)

dataBase.close()

