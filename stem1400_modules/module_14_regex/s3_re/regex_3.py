"""
regex
re.split()

"""

import re

mystr = 'Twelve:12 Eighty nine:89.'
pattern = r'\d+'

results = re.split(pattern, mystr)

print(results)
# ['Twelve:', ' Eighty nine:', '.']
