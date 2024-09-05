"""
String method - isnumeric()
True if all characters in the string are numeric characters.
False if at least one character is not a numeric character.
"""

str1 = "123456"
print(str1.isnumeric())

str1 = "1234.56"
print(str1.isnumeric())

str1 = "\u00B23455"
print(str1.isnumeric())

str1 = '\u00BD'
print(str1)
print(str1.isnumeric())