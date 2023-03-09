"""
Write a Python program to get the current time.
Sample Format :  19:19:19.078205

"""

from datetime import datetime

current_time = datetime.now()
print(current_time)

current_time = current_time.time()
print(current_time)

