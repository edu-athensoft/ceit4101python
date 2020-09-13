# any(iterable)
# The any() method takes an iterable (list, string, dictionary etc.) in Python.

# All values are true	        True
# All values are false	        False
# One value is true (others are false)	True
# One value is false (others are true)	True
# Empty Iterable	            False

# How all() works for lists?

l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

print()
print()



# How all() works for strings?
s = "This is good"
print(any(s))

# 0 is False
# '0' is True
s = '000'
print(any(s))

s = ''
print(any(s))
print()
print()



# How all() works with Python dictionaries?
# In case of dictionaries,
# if all keys (not values) are false, any() returns False.
# If at least one key is true, any() returns True.

d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))

d = {'': 'False'}
print(any(d))