"""
string method - join()

The join() string method returns a string
by joining all the elements of an iterable, separated by a string separator.

syntax:
string.join(iterable)

"""

# case 1.
numList = ['1', '2', '3', '4']
separator = ','
# separator = ';'
print(separator.join(numList))

# case 2.to change separator
numList = ['1', '2', '3', '4']
separator = ' '
# separator = '  '
print(separator.join(numList))

# case 3.to change separator
numList = ['a', 'p', 'p', 'l', 'e']
separator = ''
print(separator.join(numList))

# ex
# first name, last name = ['fname', 'lname']
studname = ['Peter', 'Jackson']
separator = ' '
print(separator.join(studname))

# ex
s1 = 'abc'
s2 = '123'
print('s1.join(s2):', s1.join(s2))

print('s2.join(s1):', s2.join(s1))
