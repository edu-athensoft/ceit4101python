"""
2.3 CRUD Operations
2.3.5 rowcount attribute
"""
import pymysql

# Establish a connection to the MySQL database
connection = pymysql.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    db='your_database'
)

try:
    # Create a cursor object
    cursor = connection.cursor()

    # Execute an SQL statement (e.g., INSERT, UPDATE, DELETE)
    sql_insert = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = ("Alice", 25)
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
