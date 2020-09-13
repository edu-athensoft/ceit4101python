"""
datetime module
timedelta class

You can also find sum of two dates and times using + operator.
Also, you can multiply and divide a timedelta object by integers and floats.
"""

# Time duration in seconds
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())

