"""
Introducing the topic of recursion

Recursion is the process of defining something in terms of itself.

This example is just a normal function call from another function.

Note: this example does not show any recursion characteristics

"""


def foo1():
    print("foo1() is called.")


def foo2():
    print("foo2() is called.")
    foo1()


foo1()
print()

foo2()





