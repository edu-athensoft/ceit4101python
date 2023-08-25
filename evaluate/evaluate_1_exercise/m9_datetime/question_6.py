"""
Write a Python program to print for the next 5 days starting from today.
"""

from datetime import date, timedelta

current_date = date.today()
print(current_date)

next_date = current_date + timedelta(days=5)
print(next_date)