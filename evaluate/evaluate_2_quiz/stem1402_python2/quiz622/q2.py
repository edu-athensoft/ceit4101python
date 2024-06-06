"""
2. Write code to change the original list to a new one as follows:
original: 	[1, 2, 3, 4, 5, 6]
new: 		[1, 5, 4, 3, 2, 6]
"""

mylist = [1, 2, 3, 4, 5, 6]
mylist[1:5] = [5, 4, 3, 2]
print(mylist)
