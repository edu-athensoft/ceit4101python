"""
yield
"""


def func():
    for i in range(0, 3):
        yield i


f = func()
print(f.__next__())
print(f.__next__())
print(f.__next__())