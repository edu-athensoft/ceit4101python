"""
write code for a progress bar with percentage


"""


"""
# auther: zeyue
import time

print("=== My Progress Bar ===")

INTERVAL = 1

for i in range(0, 21):
    print(f"\r[{i*'=':20}] {i*5}%", end="", flush=True)
    time.sleep(INTERVAL)
"""




# kevin
import time

INTERVAL = 1

print("=== My Progress Bar ===")
time.sleep(INTERVAL)
for i in range(0, 21):
    print(f"\r[{'='*i:20}]{5*i}%", end="", flush=True)
    time.sleep(INTERVAL)

