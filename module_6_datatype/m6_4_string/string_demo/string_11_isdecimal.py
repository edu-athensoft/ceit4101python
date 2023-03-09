"""
string method - isdecimal()
True - if all characters in the string are decimal characters.
False -  if at least one character is not decimal character.
"""

str1 = "1234556"
print(str1.isdecimal())

str1 = "-1234556"
print(str1.isdecimal())

str1 = "123.4556"
print(str1.isdecimal())

str1 = "123abc"
print(str1.isdecimal())

str1 = "123,333"
print(str1.isdecimal())

str1 = "1233,33"
print(str1.isdecimal())
print()

str1 = "0123"
print(str1.isdecimal())

str1 = "000000"
print(str1.isdecimal())

str2 = '2\u00B2123'
print(str2)
print(str2.isdecimal())
