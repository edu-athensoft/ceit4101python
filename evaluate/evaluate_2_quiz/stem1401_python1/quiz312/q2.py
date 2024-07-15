"""
Input a time in 24-hour style from the keyboard.
If the hour is less than 12, then the system prints out "AM";
otherwise the system prints out "PM".
The format of time is like '00:00', '09:05', '20:30'
"""


mytime = '09:05'
# mytime = '12:00'
# mytime = '00:00'
# mytime = '20:30'

if mytime < '12:00':
    print('AM')
else:
    print('PM')