"""
pytZ module
"""

from datetime import datetime
import pytz

local = datetime.now()
print("Montreal(Local):", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NewYork:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

tz_Shanghai = pytz.timezone('Asia/Shanghai')
datetime_Shanghai = datetime.now(tz_Shanghai)
print("Shanghai:", datetime_Shanghai.strftime("%m/%d/%Y, %H:%M:%S"))