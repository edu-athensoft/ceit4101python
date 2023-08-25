"""
Auto-typing
"""

import time
from pynput.keyboard import Key, Controller, KeyCode

# wait and delay
for i in range(5, 0, -1):
    print(f"{i} second(s) left")
    time.sleep(1)


mykeys = "This is an example of auto-typing. Amazing!"
keyboard = Controller()

for char in mykeys:
    keyboard.type(char)
    time.sleep(0.2)
