"""
match object

match.start()
match.end()
"""

import re

string = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

print(match, type(match))

ms = match.start()
print(f"ms={ms}")

me = match.end()
print(f"me={me}")

