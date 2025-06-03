"""
3. Write a program to convert every item in a given list
as follows and output the sum of those
 items.
 mylist = ['1', '2', '3', '4', '5']
 Hints: using lambda functions and built-in functions
"""

from functools import reduce

mylist = ['1', '2', '3', '4', '5']
# result = reduce(lambda x, y: int(x)+int(y), mylist)
result = reduce(lambda x, y: float(x)+float(y), mylist)

print(result)