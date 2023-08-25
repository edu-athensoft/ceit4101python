"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
8. Write a Python program to find the highest 3 values in a dictionary.

Hints:


"""


mydict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 5874}

# for key,value in mydict.items():
#     print(key,value)

sorted_d = sorted(mydict.items(), reverse=True, key=lambda x:x[1])
print(sorted_d)

set1 = set()
for v in mydict.values():
    set1.add(v)

a = list(set1)
a.sort(reverse=True)
print(a[0:3])
