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
USERNAME = 'appdev'
PASSWORD = 'athensoft2019'
HOST = '159.203.16.118'
PORT ='3306'
DBNAME = 'zhenzhen_db'

# title
print("SQLAlchemy - engine\n")

# create db url
DB_URL = f'{SCHEMA}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
print("DB_URL")
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
stmt = text('select item_id, item_seqno, item_code, item_status, itemsubclass_id '
            'from item_item '
            'where itemsubclass_id=:itemsubclass_id')
result = conn.execute(stmt, {'itemsubclass_id':39})
print(result)


# get data row from result
print("data row")
row = result.fetchone()
print(type(row))
print(row)
print()

# get data attribute from a row
print("attribute of a data row")
print('option 1. by [ ]')
print('row[2] =',row[2])
print()

print('option 2. by .')
print('row.item_code =',row.item_code)
print()

print('option 3. by dictionary - it is moving')
print('row["item_code"] =',row["item_code"])
print()

print('option 4. by dictionary view mapping')
print("row._mapping['item_code']",row._mapping['item_code'])
print()

# get keys of an entity
print("keys")
print(row.keys())
print(list(row.keys()))
