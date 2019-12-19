# Return Value from get()
# The get() method returns:
#
# the value for the specified key if key is in dictionary.
# None if the key is not found and value is not specified.
# value if the key is not found and value is specified.

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

# Python get() method Vs dict[key] to Access Elements
