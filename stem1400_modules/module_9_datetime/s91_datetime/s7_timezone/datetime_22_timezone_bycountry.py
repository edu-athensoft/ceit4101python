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
import pytz

timezones = pytz.country_timezones('cn')
print(timezones)

timezones = pytz.country_timezones('jp')
print(timezones)

timezones = pytz.country_timezones('kr')
print(timezones)

timezones = pytz.country_timezones('in')
print(timezones)

timezones = pytz.country_timezones('ca')
print(timezones)

timezones = pytz.country_timezones('us')
print(timezones)

timezones = pytz.country_timezones('mx')
print(timezones)

timezones = pytz.country_timezones('br')
print(timezones)

timezones = pytz.country_timezones('gb')
print(timezones)

timezones = pytz.country_timezones('de')
print(timezones)

timezones = pytz.country_timezones('fr')
print(timezones)

timezones = pytz.country_timezones('ru')
print(timezones)







