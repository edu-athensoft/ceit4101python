"""
PyMySql

create connection
and show tables
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
cursor.execute("select * from employee")

# get all records by fetchall()
resultsets = cursor.fetchall()

print(f"ResultSets:")

for record in resultsets:
    print(record)

cursor.close()

# close connection
db.close()
