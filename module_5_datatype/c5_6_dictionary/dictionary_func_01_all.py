# all()
# Return True if all keys of the dictionary are true (or if the dictionary is empty).

# All values are true	        True
# All values are false	        False
# One value is true (others are false)	False
# One value is false (others are true)	False
# Empty Iterable	            True

# How all() works for lists?

# all values true
my_dict = [1, 3, 4, 5]
print(all(my_dict))

# all values false
my_dict = [0, False]
print(all(my_dict))

# one false value
my_dict = [1, 3, 4, 0]
print(all(my_dict))

# one true value
my_dict = [0, False, 5]
print(all(my_dict))

# empty iterable
my_dict = []
print(all(my_dict))
print()
print()




# How all() works for strings?
s = "This is good"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))
print()
print()


# How all() works with Python dictionaries?
# In case of dictionaries,
# if all keys (not values) are true or the dictionary is empty, all() returns True.
# Else, it returns false for all other cases.
s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))