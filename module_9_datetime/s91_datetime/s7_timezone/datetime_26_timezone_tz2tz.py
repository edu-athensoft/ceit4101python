"""
convert local datetime to  datetime in target timezone
"""
import time
from datetime import datetime
import time
import pytz

from_timezone = pytz.timezone('America/Toronto')
to_timezone = pytz.timezone('Asia/Shanghai')


mydatetime = datetime(2022,10,12, 22, 10, 9)
mydatetime = from_timezone.localize(mydatetime)
print(mydatetime)

mydatetime = mydatetime.astimezone(tz=to_timezone)
print(mydatetime)

# epoch = time.time()
# print(epoch)

epoch = datetime.timestamp(mydatetime)
print(epoch)

