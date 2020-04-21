"""
datetime module
datetime class

"""


from datetime import datetime

a = datetime(2019, 6, 21, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("day =", a.day)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

