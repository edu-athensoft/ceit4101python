# If key is in the dictionary, return its value.
# If not, insert key with a value of d and return d (defaults to None).

# setdefault() Parameters
# key - key to be searched in the dictionary
# default_value (optional) - key with a value
#       default_value is inserted to the dictionary if key is not in the dictionary.
#       If not provided, the default_value will be None.


# Return Value from setdefault()
# value of the key if it is in the dictionary
# None if key is not in the dictionary and default_value is not specified
# default_value if key is not in the dictionary and default_value is specified


# How setdefault() works when key is in the dictionary?
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)




# How setdefault() works when key is not in the dictionary?
person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)