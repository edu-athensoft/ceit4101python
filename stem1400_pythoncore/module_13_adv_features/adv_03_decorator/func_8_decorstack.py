"""
decor stack
"""


def decor1(*param1):
    def wapper(func):
        def inner(*args):
            print("before1", param1)
            func(*args)
            print("after1")

        return inner

    return wapper


def decor2(*param2):
    def wapper(func):
        def inner(*args):
            print("before2", param2)
            func(*args)
            print("after2")

        return inner

    return wapper


@decor1("p1")
@decor2("p2", "p2b")
def foo():
    print("foo()")


foo()
