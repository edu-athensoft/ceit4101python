"""
Write a Python program to subtract five days from the current date.
Sample Date :
Current Date : 2022-08-22
5 days before Current Date : 2022-08-17

"""

from datetime import date, timedelta

current_date = date.today()
print(current_date)

last_date = current_date - timedelta(days=5)
print(last_date)