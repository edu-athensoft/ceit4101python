"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
5. Write a Python program to map two lists into a dictionary.

Hints:
zip()
dict()

"""


keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

color_dictionary = dict(zip(keys, values))
print(color_dictionary)