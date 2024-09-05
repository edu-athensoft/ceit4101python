"""
4. Using copy() and update()
First, create a copy of one dictionary and
then use the update() method to merge the other dictionary.
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



