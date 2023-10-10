"""
2.4 Batch Operations

execute multi-sql-INSERT, UPDATE, DELETE

It is required to set as follows:
client_flag=CLIENT.MULTI_STATEMENTS

"""
import pymysql
from pymysql.constants import CLIENT


# SQL statements (separated by semicolons)
sql_statements = """
INSERT INTO users (username, password) VALUES ('test-name-1', 'test-pwd-1');
UPDATE users SET password = 'test-pwd-1-new' WHERE username = 'test-name-1';
INSERT INTO users (username, password) VALUES ('test-name-2', 'test-pwd-2');
SELECT * FROM users WHERE username LIKE 'test-%';
"""

# INSERT INTO users (username, password) VALUES ('test-name-1', 'test-pwd-1');
# UPDATE users SET password = 'test-pwd-1-new' WHERE username = 'test-name-1';
# INSERT INTO users (username, password) VALUES ('test-name-2', 'test-pwd-2');

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

    # show data
    # The SELECT statement is at the 4th place, so we should move cursor for 3 times
    # otherwise results will be empty [] due to no such data set for current query
    cursor.nextset()
    cursor.nextset()
    cursor.nextset()
    results = cursor.fetchall()
    print(results)

    # Commit the transaction (if not using autocommit)
    # connection.commit()

    print("Multiple queries executed successfully.")



except pymysql.Error as e:
    print(f"Error executing queries: {e}")
    conn.rollback()
finally:
    if conn:
        # Close the cursor and the connection
        cursor.close()
        conn.close()