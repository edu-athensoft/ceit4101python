# tuple packing

my_tuple = 3, 4, 5, 6, 7
print(my_tuple, type(my_tuple))


# tuple unpacking
# a,b,c = my_tuple    # ValueError if number of tuple item > number of variables
a,b,c,d,e = my_tuple
print(a)
print(b)
print(c)

# a,b,c,d,e,f,g = my_tuple # ValueError if number of tuple item < number of variables
# print(a)
# print(b)
# print(c)