"""
Write a Python program to get the date of last Tuesday.
"""

from datetime import date, timedelta

today = date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=offset)
print(last_tuesday)
