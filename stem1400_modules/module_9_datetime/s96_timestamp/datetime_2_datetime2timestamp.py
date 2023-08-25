"""
6.2 datetime to timestamp
"""

from datetime import datetime

# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
