"""
oop mro

"""


class X(object):
    pass


class Y(object):
    pass


class A(X, Y):
    pass


class B(Y, X):
    pass

#
# class C(A, B):
#     pass



print(A.mro())
print(B.mro())