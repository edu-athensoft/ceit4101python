"""
datetime module
timedelta class

negative difference of time

"""

# Printing negative timedelta object
from datetime import timedelta

t1 = timedelta(seconds=33)
t2 = timedelta(seconds=54)
difftime = t1 - t2
print("difftime =", difftime)
print("difftime =", abs(difftime))
