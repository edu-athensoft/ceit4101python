"""
match object

match.group()
match.groups()
"""

import re

string = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

res1 = match.groups()
print(res1, type(res1))
# ('801', '35') <class 'tuple'>

res2 = match.group()
print(res2, type(res2))
# 801 35 <class 'str'>

res3 = match.group(1, 2)
print(res3, type(res3))
# ('801', '35') <class 'tuple'>

res31 = match.group(1)
print(res31, type(res31))
# 801 <class 'str'>

res32 = match.group(2)
print(res32, type(res32))
# 35 <class 'str'>

