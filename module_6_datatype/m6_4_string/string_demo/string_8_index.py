"""
string method - index

The index() method returns the index of first occurrence
of the substring (if found). If not found, it raises an ValueError
"""


str1 = 'method returns the index of first occurrence'

print(str1.index('ir'))
# print(str1.index('is'))


# with start and end arguments
print(str1.index('ir',20))
# print(str1.index('ir',20, 28))