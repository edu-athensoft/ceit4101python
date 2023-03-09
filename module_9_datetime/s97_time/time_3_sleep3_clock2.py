"""
module: datetime
class:  time
method: sleep()

# Python create a digital clock
"""

import time

"""
print(f"\ra|")
print("\r01:31:44 AM", end="", flush=True)
# print("", end="")
time.sleep(1)
print("\r01:31:45 AM", end="", flush=True)
# print("\r", end="", flush=True)
time.sleep(1)
"""

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print('\r'+result, end="", flush=True)
  # print(''+result, end="", flush=True)
  # print("\r", end="", flush=True)
  time.sleep(1)