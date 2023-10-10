"""
2.3 CRUD Operations
2.3.6 show SQL string actually sent to database
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

    # Show SQL string
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = ("Alice", '25443')
    cursor.execute(sql, values)

    sqlstr = cursor.mogrify(sql, values)
    print("Show SQL string actually sent to database")
    print(f"SQL string = {sqlstr}")

    # Commit the transaction
    connection.commit()

    # Print the result
    # print(f"Number of rows affected: {num_rows_affected}")

finally:
    # Close the cursor and the database connection
    cursor.close()
    connection.close()
