"""

"""

import time

print('=== My Progress Bar ===')

# print('[',end='')
for i in range(1, 21):
    print(f'\r[{"=" * (i - 1) + ">":20}] {i * 0.05:.0%}', end="", flush=True)
    if i == 20:
        print(f'\r[{"=" * i :20}] {i * 0.05:.0%}', end="", flush=True)
    time.sleep(0.5)

# print(']',end='')
