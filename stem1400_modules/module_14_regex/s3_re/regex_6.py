"""
regex
Program to remove all whitespaces
"""

import re

mystr = 'abc 12\
de 23 \n f45 6'

pattern = r'\s+'
replace = ''

result = re.sub(pattern, replace, mystr)
print(result, type(result))
# abc12de23f456 <class 'str'>

