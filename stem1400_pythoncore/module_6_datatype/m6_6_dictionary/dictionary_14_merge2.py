"""
2. Using the Unpacking Operator (**)
Starting from Python 3.5, you can use the unpacking operator (**) to merge dictionaries.
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

