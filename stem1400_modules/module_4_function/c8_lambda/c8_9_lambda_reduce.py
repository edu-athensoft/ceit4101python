"""
lambda

reduce()
"""

from functools import reduce


def myadd(x, y):
    return x + y


mylist = [1, 2, 3, 4, 5]
result = reduce(myadd, mylist)
print(result)
