"""
datetime module
date class

1.2.1 Current date

Get Current Weekday of today
Weekday - Mon. is 0,  Sun. is 6
ISOWeekday - Mon. is 1, Sun. is 7
"""

from datetime import date

mytoday = date.today()
print(mytoday.weekday())
print(mytoday.isoweekday())
