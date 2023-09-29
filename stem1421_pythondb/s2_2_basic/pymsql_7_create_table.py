"""
PyMySql
2.2.6 Create Database

create a db
"""

import pymysql

# settings
DB_NAME = 'stem1421_db1'

# create a connection
try:
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306,
                         database=DB_NAME)
    print('Connected successfully!')

    # create a cursor
    cursor = db.cursor()

    # execute a sql statement
    sql = "create table if not exists student(" \
          + "id int auto_increment, " \
          + "student_name varchar(20), " \
          + "school_name varchar(20), " \
          + "grade varchar(10), " \
          + "primary key (id) " \
          + ")"
    cursor.execute(sql)

    TABLE_NAME = 'student'
    print(f"Table: {TABLE_NAME} created.")

except pymysql.DatabaseError as e:
    # print('Connection failed!')
    print('Database creation failed!')

except Exception as e2:
    print("Error!")

# close cursor
cursor.close()
# close connection
db.close()
