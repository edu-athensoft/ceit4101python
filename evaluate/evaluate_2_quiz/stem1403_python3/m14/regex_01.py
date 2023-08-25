"""
Write a Python program to check that a string contains
only a certain set of characters (in this case a-z, A-Z and 0-9).
"""

import re


def contains_allowed_chars(mystr):
    pattern = r'^[a-zA-Z0-9]+$'
    # pattern = r'[a-zA-Z0-9]+'     # cannot detect underscore _
    return re.match(pattern, mystr) is not None


# Test
strings = ["Hello123", "abcXYZ", "Hello_World", "123456", "@#$%^&"]
for s in strings:
    if contains_allowed_chars(s):
        print(f"{s} contains only a-zA-Z0-9")
    else:
        print(f"{s} contains invalid characters.")
