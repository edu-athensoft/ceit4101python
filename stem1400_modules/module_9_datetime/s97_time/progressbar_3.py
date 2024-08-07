"""
write code for a progress indicator
"""

import time

INTERVAL = 0.4

print("=== My Progress Bar ===")
time.sleep(INTERVAL)
for i in range(0, 6):
    print(f"\rSearching{'.'*i:20}", end="", flush=True)
    time.sleep(INTERVAL)

