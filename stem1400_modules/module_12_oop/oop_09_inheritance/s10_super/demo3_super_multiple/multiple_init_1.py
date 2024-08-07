"""
multiple init

child has no init() method
the 1st superclass init() is called

by MRO rules,
child inherit ParentA's init() method

"""


class ParentA:
    # accessed and parameters matched
    def __init__(self):
        print('ParentA __init__() called.')


class ParentB:
    # not accessed
    def __init__(self):
        print('ParentB __init__() called.')


class Child(ParentA, ParentB):
    pass


# main
child1 = Child()


