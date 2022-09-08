"""
string

find all substring
"""

mystring = 'abcxxxabcxxxabccyyyaabc'
substring = 'abc'

# initial position
pos = 0

while True:
    pos = mystring.find(substring, pos)
    if pos > -1:
        print(pos)
        # pos += 1              # slower
        pos += len(substring)   # faster
    else:
        break