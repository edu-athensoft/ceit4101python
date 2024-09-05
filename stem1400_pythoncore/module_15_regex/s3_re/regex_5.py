"""
regex
re.split() with limit

"""

import re

mystr = 'Twelve:12 Eighty nine:89 dia 9.'
pattern = r'\d+'
maxsplit = 1

results = re.split(pattern, mystr, maxsplit)

print(results)
# ['Twelve:', ' Eighty nine:89 dia 9.']
