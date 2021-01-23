"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
4. Write a program to check whether a given key already exists in a dictionary.
Reusability should be taken into consideration.

Hints:
membership in
function

"""


def is_key_present(x):
    if x in d:
        print(f'Key: {x} is present in the dictionary')
    else:
        print(f'Key: {x} is not present in the dictionary')


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

is_key_present(5)
is_key_present(9)
