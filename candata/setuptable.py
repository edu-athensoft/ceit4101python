"""
setup tables
"""

import mydbutil
import setupdb

"""
Table: student
"""

# settings
# DB_NAME = setupdb.DB_NAME
# DB_HOST = '192.168.1.3'
# print(DB)


def create_table(sqlstr, conn, db, dbhost):
    # conn = mydbutil.get_connection(db, dbhost)
    # print(conn)
    mycursor = conn.cursor()
    mycursor.execute(sqlstr)
    print(f"[INFO] SQL: {sqlstr}")
    print(f"[INFO] Table created.")
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


# setup db
# setupdb.create_db()

# create table of student
"""
TABLE_NAME = 'student'
sql = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" \
      + "id int auto_increment, " \
      + "student_name varchar(20), " \
      + "school_name varchar(20), " \
      + "grade varchar(10), " \
      + "primary key (id) " \
      + ")"
create_table(sql)
"""
