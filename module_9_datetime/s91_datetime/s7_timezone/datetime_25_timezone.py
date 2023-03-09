"""
local time to target time in a timezone
"""

from datetime import datetime
import pytz

mydatetime = datetime(2022,10,13,13,10,9)
print(mydatetime)

tz = pytz.timezone('Asia/Jakarta')
mydatetime = datetime(2022,10,13,13,10,9,tzinfo=tz)
print(mydatetime)

tz = pytz.timezone('Asia/Shanghai')
mydatetime = datetime(2022,10,13,13,10,9,tzinfo=tz)
print(mydatetime)
