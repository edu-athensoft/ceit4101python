"""
database orm
alchemy
ver:    2.0

textual query - text()
run query .execute()
"""

from sqlalchemy import create_engine, text

# settings
SCHEMA = 'mysql+pymysql'
USERNAME = 'stemlearner'
PASSWORD = 'athensoft'
HOST = '192.168.1.3'
PORT = '3306'
DBNAME = 'stem1421pythondb'

# title
# print("SQLAlchemy - engine\n")

# create db url
DB_URL = f'{SCHEMA}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
print("DB_URL: ", end="")
print(DB_URL)
print()

# create engine
# print("engine")
engine = create_engine(DB_URL)
# print(engine)
# print()

# create connection
conn = engine.connect()

# textual query
stmt = text('select student_id, student_name, group_no '
            'from Student '
            'where student_id=:student_id')
result = conn.execute(stmt, {'student_id': 1})
# print(result)

# get data row from result
print("data row: ")
row = result.fetchone()
print(row, type(row))
print()

# get data attribute from a row
print("attribute of a data row")
print('option 1. by [ ]')
print('row[2] =', row[0])
print()

print('option 2. by .')
print('row.student_name =', row.student_name)
print()

print('option 3. by dictionary - it is moving')
print('row["group_no"] =', row["group_no"])
print()

# print('option 4. by dictionary view mapping')
# print("row._mapping['item_code']", row._mapping['item_code'])
# print()

# get keys of an entity
print("keys")
print(row.keys())
print(list(row.keys()))
print()

# closing
print("closing connection...", end="")
conn.close()
print("[Closed]")

print("closing db engine...", end="")
engine.dispose()
print("[Closed]")
