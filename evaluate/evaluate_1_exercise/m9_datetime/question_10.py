"""
Write a Python program to convert a string to datetime.
datetime.strptime()

"""

from datetime import datetime

date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)
