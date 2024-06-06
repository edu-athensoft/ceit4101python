"""
string method - isupper(), islower()

islower()
True if all alphabets that exist in the string are lowercase alphabets.
False if the string contains at least one uppercase alphabet.

"""

str1 = "python"
print(str1.islower())

str1 = "Python"
print(str1.islower())

str1 = "python."
print(str1.islower())

str1 = "python.00"
print(str1.islower())
print()
print()



str2 = "PYTHON"
print(str2.isupper())

str2 = "Python"
print(str2.isupper())

str2 = "PYTHON."
print(str2.isupper())

str2 = "PYTHON.00"
print(str2.isupper())