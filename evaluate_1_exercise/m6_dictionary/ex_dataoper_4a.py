"""
module 6.       datatype
chapter 6-6.    dictionary

Combine two dictionary adding values for common keys

Hints:
module: collections.Counter
"""


from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d = Counter(d1) + Counter(d2)
print(d)
