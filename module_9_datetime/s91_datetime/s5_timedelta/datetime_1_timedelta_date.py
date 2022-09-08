"""
datetime module
timedelta class

"""

from datetime import date

# Difference between two dates
t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)
difftime = t1 - t2

print("difftime =", difftime)
print("type of t3 =", type(difftime))
