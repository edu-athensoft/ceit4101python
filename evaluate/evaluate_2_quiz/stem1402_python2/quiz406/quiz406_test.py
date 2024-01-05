"""
quiz 406
"""


def subtract(a, b):
    print(a - b)


# q7.1
subtract(a=9, b=6)

# q7.2
subtract(b=9, a=6)

# q7.3
subtract(9, b=6)

# q7.4
# subtract(9, a=6)
# TypeError: subtract() got multiple values for argument 'a'

# q7.5
# subtract(b=9, 6)
# SyntaxError: positional argument follows keyword argument

# q15
print("---q15---")


def show(*names):
    print(names, type(names))


show('Peter', 24, 'Artist')

# q16
print("---q16---")


def foo(a, b=0, *objs):
    print(a, b, objs)


foo(1, 2, 3, 4, 5, 6, 7, 8)
foo(1)