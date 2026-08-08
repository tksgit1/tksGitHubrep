import mysql.connector

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Test@135mac',  # <-- Change to your actual password
    'database': 'testdb1'
}

# The 10 original records to insert
customer_data = [
    ('Mateo Garcia', 'Madrid', 'Singapore', 15, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 22, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 33, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 44, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 55, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 15, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 22, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 33, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 44, '91111111'),
    ('Mateo Garcia', 'Madrid', 'Singapore', 55, '91111111')
]

try:
    # 'with' ensures the connection closes safely even if the code crashes
    with mysql.connector.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            # 1. Create the table
            print("Creating table 'customer2'...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customer2 (
                    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                    FirstName VARCHAR(100) NOT NULL,
                    LastName VARCHAR(100) NOT NULL,
                    Country VARCHAR(50) DEFAULT 'Singapore',
                    Age INT,
                    Phone VARCHAR(20)
                )
            """)

            # 2. Insert the records efficiently in one batch
            print("Inserting customer records...")
            insert_query = """
                INSERT INTO customer2 (FirstName, LastName, Country, Age, Phone) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.executemany(insert_query, customer_data)

            # 3. Commit changes to lock them into the database
            conn.commit()
            print(f"Successfully inserted {cursor.rowcount} rows!")

except mysql.connector.Error as err:
    print(f"Database error: {err}")


