"""
How to add the three items at one time at the tail of the given list:
original: 	[1, 2, 3, 4, 5, 6]
items to add: 7, 8, 9

"""

mylist = [1, 2, 3, 4, 5, 6]
extra = [7, 8, 9]

mylist.extend(extra)

print(mylist)
