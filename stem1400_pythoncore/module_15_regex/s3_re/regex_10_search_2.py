"""
regex
"""

import re

mystr = "fun is fun and fun"
pattern = r'fun'

# search for 'fun'
match = re.search(pattern, mystr)
print(match, type(match))

if match:
    print("pattern found inside the string")
else:
    print("pattern not found")
