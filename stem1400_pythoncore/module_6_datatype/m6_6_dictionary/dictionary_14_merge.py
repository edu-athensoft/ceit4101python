"""
1. Using the update() Method
The update() method updates the dictionary with elements
from another dictionary object or from an iterable of key-value pairs.
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
