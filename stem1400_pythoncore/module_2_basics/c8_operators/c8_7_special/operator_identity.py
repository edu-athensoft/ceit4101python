# operator identity
# is , is not

x1 = 5
y1 = 5

print(x1, id(x1))
print(y1, id(y1))
print(x1 is y1)


x2 = "hello"
y2 = "hello"
print(x2, id(x2))
print(y2, id(y2))
print(x2 is y2)


x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3, id(x3))
print(y3, id(y3))
print(x3 is y3)



