# list copy

my_list = ['p', 'R', 'A', 'g', 'r', 'aa', 'm', 'i', 'r', 'ab']

my_list2 = my_list.copy()
print(id(my_list), id(my_list2))

# copy
my_list.sort()
print(my_list)
print(my_list2)
print()

my_list = ['p', 'R', 'A', 'g', 'r', 'aa', 'm', 'i', 'r', 'ab']

# reference
my_list_b = my_list
my_list.reverse()
print(my_list)
print(my_list_b)
