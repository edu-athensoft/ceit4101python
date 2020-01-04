"""
c7.1.5
print(flush=False|True)

reference: https://blog.csdn.net/Granthoo/article/details/82880562
"""

import time

# flush = False: not to forcibly flush the stream.
print("Loading", end="")
for i in range(16):
    print(".", end='')
    time.sleep(0.2)

print()

# flush = True: to forcibly flush the stream.
print("Loading", end="")
for i in range(16):
    print(".", end='', flush=True)
    time.sleep(0.2)

