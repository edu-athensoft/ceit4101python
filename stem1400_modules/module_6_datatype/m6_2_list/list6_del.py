# remove items

my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list)

# remove one item by index
del my_list[0]
print(my_list)

# remove multiple items
my_list = ['p','r','o','g','r','a','m','i','z']
del my_list[4:7]
print(my_list)

# delete the entire list
del my_list
# print(my_list)     # NameError

a = 27
del a
# print(a)    # NameError
