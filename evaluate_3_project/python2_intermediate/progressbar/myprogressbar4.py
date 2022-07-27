"""
loading progress bar
"""

import time

# set count-down time in second
count_down = 10

# set interval time for freshing screen in second
interval = 0.25
for i in range(0, int(count_down/interval)+1):
    print("\r"+"▇"*i+" "+str(i*10*interval)+"%", end="")
    time.sleep(interval)
print("\nLoaded.")
