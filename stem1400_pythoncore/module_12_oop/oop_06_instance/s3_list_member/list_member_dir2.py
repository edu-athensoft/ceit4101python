"""
list all members
dir(target_object)

where target_object can be literal or a variable name

"""



results = dir('111')

for member in results:
    print(member)



results = dir([])

for member in results:
    print(member)