"""
setup tables
"""

import mydbutil
import setupdb

"""
Table: student
"""

# settings
DB = setupdb.DB_NAME
# print(DB)


def create_table(sqlstr):
    conn = mydbutil.get_connection(db=DB)
    # print(conn)
    mycursor = conn.cursor()
    mycursor.execute(sqlstr)
    print(f"[INFO] SQL: {sqlstr}")
    print(f"[INFO] Table: {TABLE_NAME} created.")
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


# setup db
setupdb.create_db()

# create table of student
TABLE_NAME = 'student'
sql = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" \
      + "id int auto_increment, " \
      + "student_name varchar(20), " \
      + "school_name varchar(20), " \
      + "grade varchar(10), " \
      + "primary key (id) " \
      + ")"
create_table(sql)
