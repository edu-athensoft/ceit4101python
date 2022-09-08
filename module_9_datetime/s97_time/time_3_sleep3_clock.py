"""
module: datetime
class:  time
method: sleep()

# Python create a digital clock
"""

import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  time.sleep(1)