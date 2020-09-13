"""
module: datetime
class:  time
method: sleep()

# print a number every second
"""

import time

print("Printed immediately.")
for i in range(1,11):
    time.sleep(1)
    print(i)
