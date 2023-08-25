"""
Write a Python program to add 5 seconds with the current time.
Sample Data :
19:18:32.953088
19:18:37.953088

"""

from datetime import datetime, timedelta

current = datetime.now()
print(current)
print(current.time())

future = current + timedelta(seconds=5)
print(future)
print(future.time())