"""
datetime module
date class

get current date
get year
get month
get day
"""

# only import date class from the datetime module
from datetime import date

# Get current date
today = date.today()
print("Current date =", today)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
