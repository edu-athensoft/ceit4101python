"""
datetime module
timedelta class

"""

from datetime import datetime

# Difference between two date and time
t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
difftime = t4 - t5
print("difftime =", difftime)
print("type of t6 =", type(difftime))
