"""
function argument

function parameter, param
param list
([name1, name2, name3, name4, ....])
()
empty param list, or zero params


argument


"""


def foo1(x):
    y = x * 0.5
    return y


# half of 10
n1 = 10
print(foo1(n1))

# half of 5
print(foo1(5))

# half of -8
print(foo1(-8))

# half of 0.5
print(foo1(0.5))
