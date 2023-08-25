# methods of list

my_list = ['p','r','o','g','r','a','m','i','z','a']

# index()
# return the first matched item
result = my_list.index('a')
print(result)

# result = my_list.index('k')     # ValueError
# print(result)


# count() by value
result = my_list.count('a')
print(result)

my_list2 = [1,[2,3],[2,3]]
result = my_list2.count([2,3])
print(result)
print(my_list2[1]==my_list2[2])
print(id(my_list2[1])==id(my_list2[2]))
