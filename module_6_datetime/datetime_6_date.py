"""
datetime module
date class fromtimestamp
"""

# only import date class from the datetime module
from datetime import date

# Get date from a timestamp
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)