"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a program to sort a dictionary by value
in both ascending and descending order.

Hints:
sorted()
lambda function
dict.items()
dict()
"""

mydict = {1: 2, 3: 4, 5: 3, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',mydict)

sorted_d = dict(sorted(mydict.items(), key=lambda item:item[1]))
print('Dictionary in ascending order by value : ',sorted_d)

sorted_d = dict(sorted(mydict.items(), key=lambda item:item[1], reverse=True))
print('Dictionary in descending order by value : ',sorted_d)



