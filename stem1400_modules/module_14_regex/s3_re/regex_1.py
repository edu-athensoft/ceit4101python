"""
regex

Program to extract numbers from a string
assuming numbers here are integers
"""

import re

mystr = "hello 12 hi 89. Howdy 34"
pattern = r"\d+"

results = re.findall(pattern, mystr)
print(results, type(results))

for item in results:
    print(item)



