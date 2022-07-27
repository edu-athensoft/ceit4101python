"""
module 14. regular expression

7. Write a Python program to find sequences of lowercase letters joined with an underscore.

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

#
pattern = '^[a-z]+_[a-z]+$'

# test
isMatched(pattern, 'aaabbb')
isMatched(pattern, 'aa_bb')
isMatched(pattern, '_bbb')

isMatched(pattern, "aaa_")
isMatched(pattern, "aaa_bbb")
isMatched(pattern, "aaa__bbb")

isMatched(pattern, "a_b_c_d")
isMatched(pattern, "a_b_c")
isMatched(pattern, "a__b__c")

isMatched(pattern, "a__b_c")
isMatched(pattern, "a_b__c")