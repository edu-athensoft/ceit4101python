"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'athensoft programming'
Expected output: {}

Hints:

"""

from collections import Counter


string1 = 'aabbccddd'

d = Counter(string1)
print(d)


