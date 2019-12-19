# shadow copy
# copy()

my_dict = {1: 'apple', 2: 'ball'}

my_copy = my_dict.copy();
print(my_copy)

# prove that the two dictionary objects are not identical
print(id(my_dict), id(my_copy))

print(my_dict is my_copy)

my_copy[3]='car'
print('my_dict',my_dict)
print('my_copy',my_copy)



