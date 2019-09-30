# remove()  delete by value
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)

# pop() Output: 'o'  delete by index
my_list.pop(1)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(-1)
print(my_list)

my_list.clear()
print(my_list)
# compare it with del

my_list = ['p','r','o','b','l','e','m']
my_list[2:4] = []
print(my_list)



