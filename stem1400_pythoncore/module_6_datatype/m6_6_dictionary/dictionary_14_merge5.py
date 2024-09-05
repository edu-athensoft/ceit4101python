"""
5. Using the ChainMap from collections Module
The ChainMap class from the collections module
can also be used to merge dictionaries.
"""

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict(ChainMap(dict2, dict1))
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}




