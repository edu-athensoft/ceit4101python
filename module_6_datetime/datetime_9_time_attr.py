"""
datetime module
time class

get time attribute
"""

# only import date class from the datetime module
from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
