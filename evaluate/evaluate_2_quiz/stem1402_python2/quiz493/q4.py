"""
quiz 493
q1
"""


def outer():
    x = 99

    def inner():
        nonlocal x
        print("inner:", x)

    inner()
    print("outer:", x)


x = 33
outer()
print("outside:", x)
