"""
string method
replace(old, new)
"""

str1 = 'Happy New Year'

# Notice that str1 does not change at all
str2 = str1.replace('Happy', 'Brilliant')

print("original string is: ", str1)
print("replaced string is: ", str2)

# replace all
str3 = str1.replace('a', 'A')
print("replaced string is: ", str3)

