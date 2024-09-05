"""
regex demo 2

test a group of strings
"""

import re

def isMatched(pattern, targetstr):
    isMatched = re.match(pattern, targetstr)
    if isMatched:
        print(f"{targetstr} is matched.")
    else:
        print(f"{targetstr} is not matched.")

# main
pattern = '^a...s$'
targetstrs = ['abs', 'alias', 'abyss', 'Alias', 'An abacus']

for item in targetstrs:
    isMatched(pattern, item)
