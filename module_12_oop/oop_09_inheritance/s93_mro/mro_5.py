"""
mro 5 - hybrid inheritance
"""


class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class C1(B1, B2):
    pass


class C2(B2, B1):
    pass


# main
print(C1.__mro__)

# output
# (<class '__main__.C1'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>)

print(C2.__mro__)

# output
# (<class '__main__.C2'>, <class '__main__.B2'>, <class '__main__.B1'>, <class '__main__.A'>, <class 'object'>)
