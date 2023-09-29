"""
Db operation CRUD for student info sub-system
"""

import mydbutil
import setupdb

TABLE_NAME = 'student'


def add(student_tuple):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    # print(conn)
    mycursor = conn.cursor()
    sqlstr = f"INSERT INTO {TABLE_NAME} VALUES(%s, %s, %s, %s)"
    params = student_tuple
    mycursor.execute(sqlstr, params)
    conn.commit()
    print(f"[INFO] SQL: {sqlstr}", file=open("log.txt",'a'))
    print(f"[INFO] Record: {params} added.", file=open("log.txt",'a'))
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


def add_many(students_list):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    # print(conn)
    mycursor = conn.cursor()
    sqlstr = f"INSERT INTO {TABLE_NAME} VALUES(%s, %s, %s, %s)"
    params = students_list
    mycursor.executemany(sqlstr, params)
    conn.commit()
    print(f"[INFO] SQL: {sqlstr}")
    print(f"[INFO] Record: {params} added.")
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


def update(student_tuple):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    # print(conn)
    mycursor = conn.cursor()
    sqlstr = f"UPDATE {TABLE_NAME} SET student_name=%s, school_name=%s, grade=%s WHERE id=%s"
    params = (student_tuple[1], student_tuple[2], student_tuple[3], student_tuple[0])
    mycursor.execute(sqlstr, params)
    conn.commit()
    print(f"[INFO] SQL: {sqlstr}", file=open("log.txt",'a'))
    print(f"[INFO] Record: {params} updated.", file=open("log.txt",'a'))
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


def delete(student_id):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    # print(conn)
    mycursor = conn.cursor()
    sqlstr = f"DELETE FROM {TABLE_NAME} WHERE id=%s"
    params = (student_id,)
    mycursor.execute(sqlstr, params)
    conn.commit()
    print(f"[INFO] SQL: {sqlstr}")
    print(f"[INFO] Record: {params} deleted.")
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()


def get_by_id(student_id):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    # print(conn)
    mycursor = conn.cursor()
    sqlstr = f"SELECT * FROM {TABLE_NAME} WHERE id=%s"
    params = (student_id,)
    mycursor.execute(sqlstr, params)
    print(f"[INFO] SQL: {sqlstr}", file=open("log.txt",'a'))

    result = mycursor.fetchone()
    print(f"[INFO] {mycursor.rowcount} Record: {params} selected.", file=open("log.txt",'a'))

    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

    return result


def get_all():
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    mycursor = conn.cursor()
    sqlstr = f"SELECT * FROM {TABLE_NAME}"
    mycursor.execute(sqlstr)
    print(f"[INFO] SQL: {sqlstr}", file=open("log.txt",'a'))

    results = mycursor.fetchall()
    print(f"[INFO] {mycursor.rowcount} Record(s) selected.", file=open("log.txt",'a'))

    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

    return results




def get_by_studentname(student_name):
    conn = mydbutil.get_connection(db=setupdb.DB_NAME)
    mycursor = conn.cursor()
    sqlstr = f"SELECT * FROM {TABLE_NAME} WHERE student_name like %s"
    params = ('%'+student_name+'%',)
    mycursor.execute(sqlstr, params)
    print(f"[INFO] SQL: {sqlstr}", file=open("log.txt",'a'))

    results = mycursor.fetchall()
    print(f"[INFO] {mycursor.rowcount} Record(s) selected.", file=open("log.txt",'a'))

    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

    return results

