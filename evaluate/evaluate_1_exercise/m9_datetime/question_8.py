"""
Write a Python program to select all the Sundays of a specified year.
"""

from datetime import date, timedelta


def all_sundays(year):
    # January 1st of the given year
    dt = date(year, 1, 1)
    # First Sunday of the given year
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)


for s in all_sundays(2022):
    print(s)

