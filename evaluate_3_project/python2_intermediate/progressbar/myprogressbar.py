"""

"""

import time

print('=== My Progress Bar ===')

print('[',end='')
for i in range(20):
    print("=",end="",flush=True)
    time.sleep(1)

print(']',end='')