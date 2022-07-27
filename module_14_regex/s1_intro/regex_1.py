"""
regex demo 1
"""

import re

pattern = '^a...s$'
targetstr = 'abyss'

isMatched = re.match(pattern, targetstr)

if isMatched:
    print("Matched.")
else:
    print("Not matched.")
