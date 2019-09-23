# boolean
print('==== Data type : boolean ====')

# boolean value
print('boolean values, case sensitive')
b1 = True
print("boolean b1 = {}".format(b1))

b2 = False
print("boolean b2 = {}".format(b2))

# boolean expression
print()
print('boolean expression')
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