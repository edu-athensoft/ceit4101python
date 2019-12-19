# update a set

my_set = {1, 3}
print(my_set)

# TypeError: 'set' object does not support indexing
# my_set[0]


# add an item to a set
# add()
my_set.add(2)
print(my_set)

# add multiple items to a set
# update()
my_set.update([2, 3, 4])
print(my_set)

my_set.update((21, 31, 41))
print(my_set)

my_set.update({99,88})
print(my_set)

my_set.update({'a','b','c'}, [33, 44, 55])
print(my_set)

