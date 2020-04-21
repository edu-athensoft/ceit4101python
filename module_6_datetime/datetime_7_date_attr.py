"""
datetime module
date class
"""

# only import date class from the datetime module
from datetime import date

# Print today's year, month and day
today = date.today()
print("Current date =", today)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)