"""
Write a Python program to get current date and time in seconds with milliseconds in Python
"""

from datetime import datetime

current_datetime = datetime.now()
datetime_in_seconds = current_datetime.timestamp()
print(datetime_in_seconds)
