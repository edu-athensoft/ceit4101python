"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a Python program to print a dictionary in table format.

Hints:
zip()
"""

list1 = ['c1',1,2,3,4]
list2 = ['c2',11,12,13,14]
list3 = ['c3',111,112,113,114]

result = zip(*(list1, list2, list3))
print(result)

for row in result:
    # print(row)
    print(*row)
