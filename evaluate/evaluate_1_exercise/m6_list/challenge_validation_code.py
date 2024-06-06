"""
How to generate a validation code of 6-character length of alphabet and digit
"""

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

vcode = ''
for _ in range(6):
    vcode += random.choice(chars)

print(vcode)