"""
For efficient storage of these strings, the sequence of code points
is converted into a set of bytes. The process is known as encoding.


python uses utf-8 encoding.

syntax
string.encode(encoding='UTF-8',errors='strict')

errors - response when encoding fails.
    strict
    ignore
"""

str1 = 'pythön!'
print('The string is:', str1)

string_utf = str1.encode()
print('The encoded version is:', string_utf)