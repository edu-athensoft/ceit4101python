"""
module 6.       datatype
chapter 6-6.    dictionary


Write a Python program to iterate over dictionaries using for loops.

Hints:
for-loop
dict.items()
"""


d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])

