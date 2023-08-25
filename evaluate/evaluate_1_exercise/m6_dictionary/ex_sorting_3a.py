"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a program to sort a dictionary by value
in both ascending and descending order.

Hints:
sorted()
module: operator.itemgetter()
dict.items()
dict()
"""

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

