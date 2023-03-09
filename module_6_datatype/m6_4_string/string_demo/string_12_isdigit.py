"""
string method - isdigit()
True if all characters in the string are digits.
False if at least one character is not a digit.
"""

str1 = "1234556"
print(str1.isdigit())


str2 = '2\u00B2123'
print(str2)
print(str2.isdigit())
