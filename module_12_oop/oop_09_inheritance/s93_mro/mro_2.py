"""
mro 2 - multi-level
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


# main
print(C.__mro__)

# output
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
