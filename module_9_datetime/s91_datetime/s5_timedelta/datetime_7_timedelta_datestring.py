"""
datetime module
timedelta class

1.5.6 Time duration in seconds

You can also find sum of two dates and times using + operator.
Also, you can multiply and divide a timedelta object by integers and floats.

"""

from datetime import datetime

# Time duration in days
d1 = datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print("days = ", delta.days)
print("seconds = ", delta.seconds)
