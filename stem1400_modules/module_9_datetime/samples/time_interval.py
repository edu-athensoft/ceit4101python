"""
the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40
"""

# time interval

from datetime import *


class TimeInterval:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        td1 = timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)
        td2 = timedelta(hours=other.hours, minutes=other.minutes, seconds=other.seconds)
        td = td1 + td2
        h = td.total_seconds()//3600
        m = td.total_seconds()%3600//60
        s = td.total_seconds()%60
        return TimeInterval(h,  m, s)

    def __sub__(self, other):
        td1 = timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)
        td2 = timedelta(hours=other.hours, minutes=other.minutes, seconds=other.seconds)
        td = td1 - td2

        h = td.total_seconds()//3600
        m = td.total_seconds()%3600//60
        s = td.total_seconds()%60
        return TimeInterval(h,  m, s)

    def __str__(self):
        return f'{int(self.hours)}:{int(self.minutes)}:{int(self.seconds)}'


t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(hours=1, minutes=45, seconds=22)
t = t1 + t2
print(t)

t = t2 - t1
print(t)





