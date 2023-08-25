"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'athensoft programming'
Expected output: {}

Hints:

"""

from collections import defaultdict, Counter
str1 = 'athensoft programming'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)





