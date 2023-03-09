"""
string isprintable()

Characters that occupy printing space on the screen are known as printable characters

digits
alphabet (letters and symbols)
punctuations
whitespace
"""

# case 1.
str1 = 'Space is a printable'
print(str1)
print(str1.isprintable())
print()

# case 2.
str1 = '\nNew Line is printable'
print(str1.isprintable())
print()

# case 3.
print('case 3.')
str1 = " "
print(str1.isprintable())
print()

# case 4.
print('case 4.')
str1 = ''
print(str1.isprintable())
print()

# case 5.
# written using ASCII
print('case 5.')
str1 = str(chr(27) + chr(97))
print(str1)

if str1.isprintable():
  print('Printable')
  print(str1)
else:
  print('Not Printable')
print()

str1 = '3+3=6'
if str1.isprintable():
  print('Printable')
  print(str1)
else:
  print('Not Printable')