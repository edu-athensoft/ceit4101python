"""
sorting lists
sort()
"""

my_list = [1, 4, 2, 5, 3, 6]
my_list.sort()
print(my_list)

my_list = ['a', 'z', 'c', 'y', 'b', 'x']
my_list.sort()
print(my_list)

# my_list = [1, 'a', 2, 'z', 3, 'c', 'y', 'b', 'x']
# my_list.sort()
# print(my_list)
# TypeError: '<' not supported between instances of 'str' and 'int'

my_list = [1, 4, 2, 5, 3, 6]
my_list.sort(reverse=True)
print(my_list)
