"""
match object
"""

import re

string = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

# if match:
#     print(match.group())
# else:
#     print("pattern not found")


results = dir(match)
print(results)

# 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span',
# 'start', 'string'