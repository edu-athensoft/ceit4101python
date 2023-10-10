"""
2.4 Batch Operations

execute multi-sql-SELECT

It is required to set as follows:
client_flag=CLIENT.MULTI_STATEMENTS

"""
import pymysql
from pymysql.constants import CLIENT


# SQL statements (separated by semicolons)
sql_statements = """
SELECT * FROM users WHERE username LIKE 'test-%';
SELECT * FROM users;
"""

try:
    # connection
    conn = pymysql.connect(host='localhost', user='root', password='my123',
                           database='stem1421_db1',
                           autocommit=True,  # Enable autocommit for executing multiple queries
                           client_flag=CLIENT.MULTI_STATEMENTS,
                           charset='utf8')

    # get cursor
    cursor = conn.cursor()

    # Execute multiple queries
    cursor.execute(sql_statements)

    # get the 1st set
    results = cursor.fetchall()
    print("First data set")
    print(results)

    cursor.nextset()
    results2 = cursor.fetchall()
    print("Second data set")
    print(results2)

    print("Multiple queries executed successfully.")

except pymysql.Error as e:
    print(f"Error executing queries: {e}")
    conn.rollback()
finally:
    if conn:
        # Close the cursor and the connection
        cursor.close()
        conn.close()