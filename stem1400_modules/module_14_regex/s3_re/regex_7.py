"""
regex
re.sub(pattern, replace, mystr, times)
Program to remove all whitespaces
"""

import re

mystr = 'abc 12\
de 23 \n f45 6'

pattern = r'\s+'
replace = ''
times = 3

result = re.sub(pattern, replace, mystr, times)
print(result, type(result))
# abc12de23f45 6 <class 'str'>

