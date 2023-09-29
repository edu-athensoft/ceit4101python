"""
2.4 Batch Operations

delete in batch
sql statement with parameters
cursor.executemany(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='test', charset='utf8')

# get cursor
cursor = conn.cursor()

# delete in batch
sql = "DELETE FROM users WHERE id = %s"
params = [(1,), (2,), (3,)]
cursor.executemany(sql, params)


# commit transaction
conn.commit()

# close
cursor.close()
conn.close()