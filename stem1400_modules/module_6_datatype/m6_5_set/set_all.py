# set all
# True == 1,  False = 0

my_list = [1, 2, 3, 4, 5]
print(all(my_list))

my_list = [1, 2, 3, 4, 0]
print(all(my_list))

my_list = [-1, -2, -3, -4, -5]
print(all(my_list))

my_list = [-1, -2, -3, -4, False]
print(all(my_list))

my_list = []
print(all(my_list))