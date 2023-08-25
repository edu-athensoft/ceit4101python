# set method

my_set = {1,2,3,4,5}
result = my_set.copy()
print(result)

print(id(my_set), id(result))

print(my_set == result) # by value
print(my_set is result) # by reference/address
