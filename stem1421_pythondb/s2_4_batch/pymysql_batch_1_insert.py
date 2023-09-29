"""
2.4 Batch Operations

insert in batch
sql statement with parameters
cursor.executemany(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='test', charset='utf8')

# get cursor
cursor = conn.cursor()

# insert in batch
sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
params = [('Tom', '123456'), ('Jerry', '654321'), ('Alice', '111111')]
cursor.executemany(sql, params)

# commit transaction
conn.commit()

# close
cursor.close()
conn.close()