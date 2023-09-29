"""
PyMySql

create connection
insert records
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

sql= "UPDATE employee set email='mark222@gmail.com' WHERE email = 'mark@gmail.com'"

try:
    # execute a sql statement
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()

# close cursor
cursor.close()

# close connection
db.close()
