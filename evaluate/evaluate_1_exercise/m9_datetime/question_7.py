"""
Write a Python program to get a week number of a year with a given date.
Sample Date : 2015, 6, 16
Expected Output : 25

https://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python
datetime.date has a isocalendar() method, which returns a tuple containing the calendar week

In Python 3.9+ isocalendar() returns a namedtuple with the fields year, week and weekday

"""

from datetime import date

mydate  = date(2015, 6, 16)
result = mydate.isocalendar()
print(result)

# test on python 3.9+
# print(result.year)
# print(result.week)
# print(result.weekday)

mydate  = date.today()
result = mydate.isocalendar()
print(result)
