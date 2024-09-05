"""
return statement

return multiple values
"""


# return multiple values
def foo1():
    x = 1
    y = 2
    return x, y


a, b = foo1()
print(f'foo1() returned multiple values: a={a}, b={b}')

# auto-packed as a tuple
tuple1 = foo1()
print(f'foo1() returned as one tuple: {tuple1}')

