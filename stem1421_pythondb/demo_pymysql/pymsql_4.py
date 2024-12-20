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

sql= "INSERT INTO employee(name,email,phone,city,working_hours) " \
     "VALUES ('Bill','bill@gmail.com','438-222-2345','Montreal',7)"

try:
    # execute a sql statement
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# close cursor
cursor.close()

# close connection
db.close()
