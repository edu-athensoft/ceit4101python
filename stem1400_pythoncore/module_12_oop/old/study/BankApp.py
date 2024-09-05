import stem1400_pythoncore.module_12_oop.old.study.Bank as Bank


print("=== init ===")

# Athens' bank account object
b1 = Bank.BankAccount('001', 'Athens', 8000)
# print(b1)
print("Account Info. of",b1.accountName)
print(b1.accountId, b1.accountName, b1.balance)
print()
# print(b1.accountId)
# print(b1.accountName)
# print(b1.balance)

# Jovy's bank account object
b2 = Bank.BankAccount('002', 'Jovy', 9000)
# print(b2)
print("Account Info. of",b2.accountName)
print(b2.accountId, b2.accountName, b2.balance)
# print(b2.accountName)
# print(b1.balance)

print()
print("=== transaction 1. Athens deposited 200$ ===")
# transaction 1. Athens deposited 200$
b1.deposit(200)
print(b1.accountName,b1.balance)

print()
print("=== transaction 2. Jovy withdrew 200$ ===")
# transaction 2. Jovy withdrew 200$
b2.withdraw(200)
print(b2.accountName,b2.balance)

print()
print("=== transaction 3. Athens e-transferred 500$ to Jovy ===")
# transaction 3. Athens e-transferred 500$ to Jovy
b1.withdraw(500)
b2.deposit(500)
print(b1.accountName,b1.balance)
print(b2.accountName,b2.balance)

print()
print("=== comparing ===")
print("b1<b2?",b1<b2)
print("b1>b2?",b1>b2)
print("b1=",b1)
print("b2=",b2)


print()
print("=== id ===")
print("id of b1: ",id(b1))
print("id of b2: ",id(b2))