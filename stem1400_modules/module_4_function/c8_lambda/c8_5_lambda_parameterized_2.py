"""
Lambda Function

parameterized
"""


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(20))
