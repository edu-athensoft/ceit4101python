x = True
y = False

print("x={}, y={}".format(x,y))

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)


# boolean expression
print()
print('boolean expression')
b1 = False
b2 = True

expr1 = b1 and b2
print("b1 and b2 = {}".format(expr1))

expr2 = b1 or b2
print("b1 or b2 = {}".format(expr2))

expr3 = not b1
print("not b1 = {}".format(expr3))

expr4 = not b1 and b2
print("not b1 and b2 = {}".format(expr4))

expr5 = not (b1 and b2)
print("not b1 and b2 = {}".format(expr5))

expr6 = 5 > 3
print("5 > 3 is {}".format(expr6))