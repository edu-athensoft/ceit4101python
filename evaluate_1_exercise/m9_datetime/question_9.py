"""
Write a Python program to find the date of the first Monday of a given week
"""

import time

print(time.asctime(time.strptime('2022 40 1', '%Y %W %w')))
