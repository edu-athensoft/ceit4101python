"""
match object

match.re
"""

import re

string = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

print(match, type(match))

res = match.re
print(f"match.re = {res}")
# output: re.compile('(\\d{3}) (\\d{2})')

