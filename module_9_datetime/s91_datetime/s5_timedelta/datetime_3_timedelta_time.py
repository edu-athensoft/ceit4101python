"""
datetime module
timedelta class

DOES NOT SUPPORT
TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'

"""

from datetime import time

# Difference between two dates
t1 = time(hour=20, minute=18, second=16)
t2 = time(hour=19, minute=17, second=15)
difftime = t1 - t2

print("difftime =", difftime)
print("type of difftime =", type(difftime))
