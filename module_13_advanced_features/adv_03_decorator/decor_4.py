"""
decorator
with @ symbol

AOP like decorator
around advice
pre advice
post advice
"""


def aroundadvice(fn):
    def wrapper(*args, **kwargs):
        print("INFO: before", fn.__name__)
        fn(*args, **kwargs)
        print("INFO: after", fn.__name__)
    return wrapper


def preadvice(fn):
    def wrapper(*args, **kwargs):
        print("INFO: pre advice", fn.__name__)
        fn(*args, **kwargs)
    return wrapper


def postadvice(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        print("INFO: post advice", fn.__name__)
    return wrapper


@aroundadvice
def foo1():
    print("this is foo1()")


@preadvice
def foo2():
    print("this is foo2()")


@postadvice
def foo3():
    print("this is foo3()")

# test
foo1()
print()

foo2()
print()

foo3()
print()

