"""
iterable
"""

mylist = [1, 2, 3]

# get iterator of an iterable object
mylist_iterator = iter(mylist)

# ok
print(next(mylist_iterator))
print(next(mylist_iterator))
print(next(mylist_iterator))

# exception
print(next(mylist_iterator))


