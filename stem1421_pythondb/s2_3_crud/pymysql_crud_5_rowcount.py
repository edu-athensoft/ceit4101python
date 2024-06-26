"""
2.3 CRUD Operations
2.3.5 rowcount attribute
"""
import pymysql

# Establish a connection to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='my123',
    db='stem1421_db1'
)

try:
    # Create a cursor object
    cursor = connection.cursor()

    # Execute an SQL statement (e.g., INSERT, UPDATE, DELETE)
    sql_insert = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = ("Alice", '25443')
    cursor.execute(sql_insert, values)

    # Get the number of rows affected by the INSERT statement
    num_rows_affected = cursor.rowcount

    # Commit the transaction
    connection.commit()

    # Print the result
    print(f"Number of rows affected: {num_rows_affected}")

finally:
    # Close the cursor and the database connection
    cursor.close()
    connection.close()
