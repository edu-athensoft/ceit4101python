"""
mro 3 - hierarchical
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


# main
print(B.__mro__)

# output
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

print(C.__mro__)

# output
# (<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
