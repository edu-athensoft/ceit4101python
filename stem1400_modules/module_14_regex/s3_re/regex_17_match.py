"""
re.compile()
"""

import re

mystr = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'\d{3} \d{2}'

# directly compile a regex strin
# res = re.compile(pattern)
# print(res, type(res))

match_obj = re.compile(pattern).match(mystr, 2)
print(match_obj)



