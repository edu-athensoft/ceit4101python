# list concatenation

my_list = [1,2,3]
my_list2 = ['a','b','c']
result = my_list + my_list2
print(result, id(result), id(my_list), id(my_list2))

result2 = my_list * 3
print(result2)
