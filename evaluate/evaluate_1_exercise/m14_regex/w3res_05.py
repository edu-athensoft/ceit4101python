"""
module 14. regular expression

5. Write a Python program that matches a string that has an a followed by three 'b'.

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

# ending with three letter b, starting with any character
pattern = '^.b{3}$'

# test
isMatched(pattern, 'abbb')
isMatched(pattern, 'cb')
isMatched(pattern, 'c')

isMatched(pattern, "ac")
isMatched(pattern, "abc")
isMatched(pattern, "a")

isMatched(pattern, "ab")
isMatched(pattern, "abb")
