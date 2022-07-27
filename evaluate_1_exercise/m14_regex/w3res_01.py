"""
module 14. regular expression

1. Write a Python program to check that a string contains only a
certain set of characters (in this case a-z, A-Z and 0-9).

source: https://www.w3resource.com/python-exercises/re/index.php
"""
import re


def isMatched(pattern, mystr):
    ismatched = re.match(pattern, mystr)
    if ismatched:
        print(mystr, "matched.")
    else:
        # print(mystr, "not matched.")
        pass


pattern = '[a-zA-Z0-9]'

# test
isMatched(pattern, 'abc123ABC')
isMatched(pattern, 'abc12_3ABC')
isMatched(pattern, '-)(\&%%\$\^')
