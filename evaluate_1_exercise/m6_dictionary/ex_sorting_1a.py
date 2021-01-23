"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a program to sort a dictionary by key
in both ascending and descending order.

Hints:
sorted()
dict.items()
dict()
"""

import operator
d = {'ca': 2, 'ab': 4, 'bb': 3, 'b': 1, 'aa': 0}
print('Original dictionary : \n',d)
print()

sorted_d = dict(sorted(d.items()))
print('Dictionary in ascending order by value : \n',sorted_d)
print()

sorted_d = dict(sorted(d.items(), reverse=True))
print('Dictionary in descending order by value : \n',sorted_d)

