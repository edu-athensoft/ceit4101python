# explicit conversion

# a = 123
# b = "456"
# c = a + b
# print(c)


a = 123
b = "456"
c = str(a) + b
print(c, type(c))

a = 123
b = "456"
c = a + int(b)
print(c, type(c))

a = 123
b = "456"
c = a + float(b)
print(c, type(c))