"""
return statement

return single value
"""


# return a value
def foo1():
    return 1


# return a variable
def foo2():
    x = 2
    return x


# return an expression
def foo3():
    x = 2
    return x + 1


# test
print(f'foo1() returned {foo1()}')

print(f'foo2() returned {foo2()}')

print(f'foo3() returned {foo3()}')
