"""
datetime module
timedelta class

1.5.6 Time duration in seconds

You can also find sum of two dates and times using + operator.
Also, you can multiply and divide a timedelta object by integers and floats.

"""

from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

delta = timedelta(days=3)
n_days = now + delta
print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
