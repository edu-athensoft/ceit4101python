"""
string method - find

The find() method returns the index of first occurrence
of the substring (if found). If not found, it returns -1.
"""

str1 = 'method returns the index of first occurrence'

print(str1.find('is'))

if str1.find('is') == -1:
    print("no such substring in the original string")


# with start and end arguments
print(str1.find('ir',20))
print(str1.find('ir',20, 28))