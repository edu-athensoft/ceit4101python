# remove items from a set

# remove an item
# discard()
# removed()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# using discard()
my_set.discard(6)
print(my_set)

my_set.discard(6)
print(my_set)


my_set = {1, 3, 4, 5, 6}
# using discard()
my_set.remove(6)
print(my_set)

# my_set.remove(6)    # KeyError
# print(my_set)



# remove an item and return the value
# pop()
# It is completely arbitrary
my_set = {'b', 1, 3, 4, 5, 6}
item = my_set.pop()
print(item)

item = my_set.pop()
print(item)

item = my_set.pop()
print(item)

item = my_set.pop()
print(item)


# remove all element from a set
my_set.clear()
print(my_set)


