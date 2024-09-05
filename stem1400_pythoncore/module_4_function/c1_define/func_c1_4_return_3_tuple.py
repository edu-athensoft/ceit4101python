"""
return statement

return a tuple, not recommended
"""


# return a tuple, not recommended
def foo1():
    x = 1
    y = 2
    return (x, y)


tuple1 = foo1()
print(f'foo1() returned as one tuple: {tuple1}')

a, b = foo1()
print(f'foo1() returned multiple values: a={a}, b={b}')
