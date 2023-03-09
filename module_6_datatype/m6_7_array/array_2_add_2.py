"""
Python array
Adding Elements to a Array

append()
extend()

source:
"""

import array as arr
numbers = arr.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)     # Output: array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])
