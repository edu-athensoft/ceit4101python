"""
How to generate a validation code of 6-character length of alphabet and digit
"""

import random
import string

chars = string.ascii_letters + string.digits
# print(chars)

vcode = ''
for _ in range(6):
    vcode += random.choice(chars)

print(vcode)