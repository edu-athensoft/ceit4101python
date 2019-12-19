grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))
print(enumerateGrocery)

my_list = list(enumerateGrocery)
print(my_list)

print(my_list[0])


# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))