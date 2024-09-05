"""
regex
re.subn(pattern, replace, mystr)

"""

import re

mystr = 'abc 12\
de 23 \n f45 6'

pattern = r'\s+'
replace = ''

result = re.subn(pattern, replace, mystr)
print(result, type(result))
# ('abc12de23f456', 4) <class 'tuple'>
