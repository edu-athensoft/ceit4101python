"""
module 6.       datatype
chapter 6-6.    dictionary

Combine two dictionary adding values for common keys

Hints:
module: collections.Counter
dict.keys()
dict.values()
for-loop
"""


from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for key2 in d2.keys():
    if key2 in d1.keys():
        d1[key2] += d2[key2]
    else:
        d1[key2] = d2[key2]

print(d1)
