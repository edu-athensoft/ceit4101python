"""
PyMySql
Transcation

commit and rollback
"""

import pymysql

# settings
DB_NAME = 'stem1421_db1'


# create a connection
def transfer(amount, account1_id, account2_id):
    try:
        conn = pymysql.connect(host='localhost',
                             user='root',
                             passwd='my123',
                             port=3306,
                             database=DB_NAME,
                             autocommit=False)
        # Disable autocommit to use transactions
        # print('Connected successfully!')

        # create a cursor
        cursor = conn.cursor()

        # transfer money from personal cheque account to savings account

        # Check the balance of account1
        cursor.execute("SELECT balance FROM account WHERE id = %s", account1_id)
        account1_balance = cursor.fetchone()[0]
        print(account1_balance)

        if account1_balance < amount:
            raise Exception("Insufficient funds in account1")

        # Deduct the amount from account1
        cursor.execute("UPDATE account SET balance = balance - %s WHERE id = %s", (amount, account1_id))

        # Add the amount to account2
        cursor.execute("UPDATE account SET balance = balance + %s WHERE id = %s", (amount, account2_id))

        # before commit(), it takes effect.
        raise pymysql.DatabaseError("Rolling back!")

        # Commit the transaction
        conn.commit()

        print(f"Money of ${amount} dollars transferred from account:{account1_id} to account:{account2_id}")
        print(f"Transaction done!")



    except pymysql.DatabaseError as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print(f"Transaction failed: {e}")
    except Exception as e2:
        print("Error!")
        print(e2)
    finally:
        cursor.close()
        conn.close()


# test
peter_amount = 100
peter_account1_id = 1
peter_account2_id = 2
transfer(peter_amount, peter_account1_id, peter_account2_id)