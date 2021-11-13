"""
Auto-press key
"""
import time
from pynput.keyboard import Key, Controller, KeyCode

# wait and delay
for i in range(5, 0, -1):
    print(f"{i} second(s) left")
    time.sleep(1)


# Keyboard controller object
keyboard = Controller()

# press key 'a'
keyboard.press('a')
# release key 'a'
keyboard.release('a')

# press key 'Shift'
keyboard.press(Key.shift)
keyboard.press('b')
keyboard.release('b')
keyboard.press('c')
keyboard.release('c')
# release key 'Shift'
# keyboard.release(Key.esc)
keyboard.release(Key.shift)

# Press down the key 'Shift'
# then press other keys respectively
# release 'Shift' when finishing
with keyboard.pressed(Key.shift):
    keyboard.press('d')
    keyboard.release('d')
    keyboard.press('e')
    keyboard.release('e')

# press the key sequence of ' python' (including leading whitespace)
keyboard.type(' python')

# press key whose vk=56,  shift
keyboard.touch(KeyCode.from_vk(56), True)
keyboard.touch('a', True)
keyboard.touch('a', False)

# release key 'Shift'
keyboard.touch(Key.shift, False)