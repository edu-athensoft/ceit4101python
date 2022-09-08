"""
datetime module
timedelta class

"""

from datetime import timedelta

# Difference between two timedelta objects
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
difftime = t1 - t2

print("difftime =", difftime)
