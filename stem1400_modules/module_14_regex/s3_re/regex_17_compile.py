"""
re.compile()
"""

import re

# string = '39801 356, 2102 1111'

# Three-digit number followed by space followed by two-digit number
pattern = r'(\d{3}) (\d{2})'

# directly compile a regex string
res = re.compile(pattern)
print(res, type(res))
# re.compile('(\\d{3}) (\\d{2})') <class 're.Pattern'>


