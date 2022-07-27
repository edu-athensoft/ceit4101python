"""
mro 1 - single
"""


class A:
    pass


class B(A):
    pass


# main
print(B.__mro__)

# output
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
