"""
datetime module
date class fromtimestamp

A Unix timestamp is the number of seconds
between a particular date and January 1, 1970 at UTC.

"""

# only import date class from the datetime module
from datetime import date

# Get date from a timestamp
timestamp = date.fromtimestamp(1606244364)
print("Date =", timestamp)