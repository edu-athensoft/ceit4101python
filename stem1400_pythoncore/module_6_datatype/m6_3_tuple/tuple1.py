# create/declare/define

my_tuple = (1,2,3)
print(my_tuple, type(my_tuple))

# create an empty tuple
my_tuple = ()  # []
print(my_tuple, type(my_tuple))

# create a tuple with only one item
my_tuple = (1,)
print(my_tuple, type(my_tuple))

# create a mix tuple
my_tuple = (1,2,'b',3,'c')
print(my_tuple)

# create a nested tuple
my_tuple = (1,2,[33,44,55],3,'c')
print(my_tuple)

my_tuple = (1,2,[33,44,55],('aa','bb','cc'),'c')
print(my_tuple)
