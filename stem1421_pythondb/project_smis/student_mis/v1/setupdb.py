"""
init database: smis
"""

import mydbutil as dbutil

DB_NAME = 'smis'


def create_db(database=DB_NAME):
    if database:
        conn = dbutil.get_connection()
        # print(f'[INFO] {conn}')

        mycursor = conn.cursor()
        sql = f"CREATE DATABASE IF NOT EXISTS {database}"
        mycursor.execute(sql)
        print(f"[INFO] SQL: {sql}")
        print(f'[INFO] Database:{database} created.')

        if mycursor:
            mycursor.close()
        if conn:
            conn.close()

    else:
        print("[WARNING] Database name is missing! ")


def drop_db(database=DB_NAME):
    conn = dbutil.get_connection(database)
    # print(f'[INFO] {conn}')

    mycursor = conn.cursor()
    sql = f"DROP DATABASE IF EXISTS {database}"
    mycursor.execute(sql)

    print(f'[INFO] Database:{database} deleted.')

    if conn:
        conn.close()
    if mycursor:
        mycursor.close()


# test create_db()
# create_db()

# test drop_db()
# drop_db()
