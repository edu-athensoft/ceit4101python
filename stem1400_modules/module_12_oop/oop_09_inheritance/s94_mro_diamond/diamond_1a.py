"""
diamond problem 1
"""


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass


# main
print(D.__mro__)

d1 = D()
d1.m()
