"""
Please calculate how much time is required for travellers
go from Montreal to Shanghai according to the a flight ticket as below.
"""

from datetime import datetime, timedelta
import pytz

dep_timezone = pytz.timezone("America/Toronto")
arr_timezone = pytz.timezone("Asia/Shanghai")

# departure date and time
dep_date = datetime(2022, 11, 2, 21, 30, 0)
arr_date = datetime(2022, 11, 4, 6, 40, 0, tzinfo=arr_timezone)


dt_dep = dep_date.astimezone(dep_timezone)
print(dt_dep)
print(arr_date.astimezone(arr_timezone))

# arrival time in montreal timezone
dt_arr = arr_date.astimezone(dep_timezone)
print(dt_arr)

# time diff
time_escaped = dt_arr - dt_dep
print(time_escaped)

print('days',time_escaped.days)
print('seconds',time_escaped.seconds)
print('hours:minutes',time_escaped.seconds//3600, time_escaped.seconds%3600//60)







