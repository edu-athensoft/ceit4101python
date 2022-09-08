"""
pytZ module

timezone list
http://pytz.sourceforge.net/#what-is-utc


There are two lists of timezones provided.
all_timezones is the exhaustive list of the timezone names that can be used.

common_timezones is a list of useful, current timezones.
It doesn’t contain deprecated zones or historical zones, except for a few I’ve deemed in common usage, such as US/Eastern (open a bug report if you think other timezones are deserving of being included here). It is also a sequence of strings
"""

from datetime import datetime
# import pytz
from pytz import all_timezones

len_of_timezone = len(all_timezones)
print("all_timezones has {} time zones.".format(len_of_timezone))

for tz in all_timezones:
    print(tz)





