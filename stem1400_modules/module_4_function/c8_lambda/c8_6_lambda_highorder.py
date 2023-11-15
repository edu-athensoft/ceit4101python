"""
High Order Function
lambda as parameter
"""

f = lambda x, a: a * x + a


def myfunc(f, x, a):
    return f(x, a)


print(myfunc(f, 1, 3))

print(myfunc(f, 2, 3))
