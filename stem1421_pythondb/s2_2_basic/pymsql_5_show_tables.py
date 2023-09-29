"""
PyMySql
3.4 Show DB version

show tables of a selected db
"""

import pymysql

# create a connection
try:
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306,
                         database='abccompany')
    print('Connected successfully!')
except pymysql.DatabaseError as e:
    print('Connection failed!')

# create a cursor
cursor = db.cursor()

# execute a sql statement
cursor.execute("show tables")

# get a single result set by fetchone()
dataset = cursor.fetchone()

print(f"Tables : {dataset}")

cursor.close()

# close connection
db.close()
