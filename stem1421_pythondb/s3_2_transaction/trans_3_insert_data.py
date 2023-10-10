"""
PyMySql
Insert data
"""

import pymysql

# settings
DB_NAME = 'stem1421_db1'

# create a connection
try:
    conn = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306,
                         database=DB_NAME)
    # print('Connected successfully!')

    # create a cursor
    cursor = conn.cursor()

    # execute sql statements
    sql = "insert into account(client_name, acct_name, balance, trans_date) values(%s, %s, %s, %s)"
    params = [('Peter','Personal Cheque', 3000, '2023-09-28'),
              ('Peter','Personal Savings', 5000, '2023-09-28'),
              ('Jack', 'Personal Cheque', 2000, '2023-09-28'),
              ('Jack', 'Personal Savings', 4000, '2023-09-28')]
    cursor.executemany(sql, params)

    # commit() is required
    conn.commit()

    TABLE_NAME = 'account'
    print(f"Records were inserted into {TABLE_NAME}.")

except pymysql.DatabaseError as e:
    print('Database creation failed!')

except Exception as e2:
    print("Error!")
finally:
    cursor.close()
    conn.close()

