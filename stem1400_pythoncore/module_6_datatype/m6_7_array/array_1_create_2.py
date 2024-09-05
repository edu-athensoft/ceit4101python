"""
create an array
"""

import array as arr

myarr = arr.array("i")

# how many bytes does an item take in the memory?
print(myarr.itemsize)


myarr = arr.array("i", range(5))
print(len(myarr))
