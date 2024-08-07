"""
progress bar

"""

import time

print("=== My Progress Bar ===")
print("[", end="")

INTERVAL = 0.25

for i in range(20):
    print("=", end="")
    time.sleep(INTERVAL)

print("]")
