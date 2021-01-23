"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
8. Write a Python program to find the highest 3 values in a dictionary.

Hints:
module: heapq.nlargest

"""

from heapq import nlargest

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 5874,}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)
