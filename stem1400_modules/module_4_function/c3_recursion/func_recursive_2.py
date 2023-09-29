"""
Recursion is the process of defining something in terms of itself.

Recursive function
"""


def foo2():
    print("foo2() is called.")
    foo2()


foo2()
# RecursionError: maximum recursion depth exceeded while calling a Python object






