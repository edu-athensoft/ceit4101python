"""
show datetime and milli-second
"""

from datetime import datetime

# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))