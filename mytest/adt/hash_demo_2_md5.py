"""
issue
difference hash values occur in different command line shell environment

original source:
https://www.cnblogs.com/liangmingshen/p/13207765.html
"""

import hashlib

data = 'Nobody inspects the spammish repetition'

v1 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
print(v1)
