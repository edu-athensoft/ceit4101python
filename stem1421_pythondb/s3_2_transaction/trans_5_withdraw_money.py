"""
PyMySql
Transcation

commit and rollback
"""

import pymysql

# settings
DB_NAME = 'stem1421_db1'


def withdraw(amount, account1_id):
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

        # withdraw money from personal cheque account

        # Check the balance of account1
        cursor.execute("SELECT balance FROM account WHERE id = %s", account1_id)
        account1_balance = cursor.fetchone()[0]

        if account1_balance < amount:
            raise Exception("Insufficient funds in account1")

        # Deduct the amount from account1
        cursor.execute("UPDATE account SET balance = balance - %s WHERE id = %s", (amount, account1_id))

        # Commit the transaction
        conn.commit()

        print(f"Money of ${amount} dollars withdrawn from account:{account1_id}")
        print(f"Transaction done!")


    except pymysql.DatabaseError as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print(f"Transaction failed: {e}")
    except Exception as e2:
        print("Error!")
    finally:
        cursor.close()
        conn.close()


# test
jack_amount = 100
jack_account1_id = 3
withdraw(jack_amount, jack_account1_id)
