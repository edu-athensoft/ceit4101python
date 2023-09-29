"""
2.4 Batch Operations

update in batch
sql statement with parameters
cursor.executemany(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='test', charset='utf8')

# get cursor
cursor = conn.cursor()

# update in batch
sql = "UPDATE users SET password = %s WHERE username = %s"
params = [('123456', 'Tom'), ('654321', 'Jerry'), ('111111', 'Alice')]
cursor.executemany(sql, params)


# commit transaction
conn.commit()

# close
cursor.close()
conn.close()