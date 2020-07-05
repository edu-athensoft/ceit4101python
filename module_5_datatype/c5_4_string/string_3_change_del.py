"""
string - changing or delete
"""
# string - delete

my_string = 'athensoft inc'
print(my_string)

# changing element is not allowed
# my_string[5] = 'a'      # TypeError

# reassign is allowed
my_string = 'Python'
print(my_string)


# del a char?  no way
# not allowed
# del my_string[5]        # TypeError

# allowed
del my_string              # works
print(my_string)           # NameError