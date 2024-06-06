"""
string method - isidentifier()
returns True if the string is a valid identifier in Python.
If not, it returns False.

"""

str1 = "Python"
print(str1.isidentifier())

str1 = "True"
print(str1.isidentifier())

str1 = "Py thon"
print(str1.isidentifier())

str1 = "0abc"
print(str1.isidentifier())

str1 = "_0abc"
print(str1.isidentifier())

str1 = "$0abc"
print(str1.isidentifier())

str1 = "-0abc"
print(str1.isidentifier())




