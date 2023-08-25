"""
regex
"""

import re

mystr = "Python is fun"
pattern = r'\APython'

# check if 'Python' is at the beginning
match = re.search(pattern, mystr)
print(match, type(match))

if match:
    print("pattern found inside the string")
else:
    print("pattern not found")
