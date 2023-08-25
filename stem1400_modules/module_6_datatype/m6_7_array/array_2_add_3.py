"""
Python array
concatenate

typecodes = 'bBuhHiIlLqQfd'

source:
"""

import array as arr
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])

numbers = arr.array('i')   # creating empty array of integer
numbers = odd + even
print(numbers)

