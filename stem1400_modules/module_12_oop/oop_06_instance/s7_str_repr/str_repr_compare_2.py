"""
__str__ vs __repr__

"""

import datetime

now = datetime.datetime.now()

print("__str__()")
print(now.__str__())

print("__repr__()")
print(now.__repr__())



