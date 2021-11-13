"""
The constructor is called when the object is being created

The constructor can be manually called

Explicitly calling a constructor returns None
A constructor should return None
"""

import module_12_oop.old.study.Bank as Bank


print("=== init ===")

# bank account object
b1 = Bank.BankAccount('001', 'Athens', 8000)
print("Account Info. of",b1)
print()

# bank account object
b1.__init__('002','Jovy',8080)
print("Account Info. of",b1)
print()

# bank account object
# Explicitly calling a constructor returns None
obj1 = b1.__init__('002','Jovy',8080)
print("obj1:",obj1)
print(type(obj1))


