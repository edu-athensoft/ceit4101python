"""
string method - isspace()

- spaces
- tabs
- new lines

"""

s1 = '   \t'
print(s1.isspace())

s2 = ' a '
print(s2.isspace())

s3 = ''
print(s3.isspace())

# case 1.
s = '\t  \n'
if s.isspace():
  print('All whitespace characters')
else:
  print('Contains non-whitespace characters')