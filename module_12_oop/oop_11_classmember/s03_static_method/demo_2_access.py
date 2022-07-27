"""
accessing a static method
"""


class Foo:
    @staticmethod
    def myMethod():
        print("myMethod() was invoked.")


# test
Foo.myMethod()
