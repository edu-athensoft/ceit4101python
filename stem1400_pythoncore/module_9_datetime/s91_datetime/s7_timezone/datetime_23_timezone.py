"""
get date and time by timezone
"""

from datetime import datetime
import pytz

mydatetime = datetime.now()
print(mydatetime)

tz = pytz.timezone('Asia/Jakarta')
mydatetime = datetime.now(tz)
print(mydatetime)

tz = pytz.timezone('Asia/Shanghai')
mydatetime = datetime.now(tz)
print(mydatetime)

tz = pytz.timezone('UTC')
mydatetime = datetime.now(tz)
print(mydatetime)