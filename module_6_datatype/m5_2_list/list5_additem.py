# list adding item(s)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

# append()
my_list.append(10)
print(my_list)

# extend()
my_list.extend([11])
print(my_list)

my_list.extend([12,13,14,15])
print(my_list)

# my_list.extend(11) # TypeError
# print(my_list)


# insert
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.insert(2,88)
print(my_list)
# output: 1,2,88,3,4,5,6,7,8,9

# insert a nested list as one item
my_list.insert(2,[55,66])
print(my_list)

# insert multiple items
my_list[2:2] = ['a','b','c']
print(my_list)