"""
multiple init

child has its own init() method

by MRO rules,
child called its own init() method

"""


class ParentA:
    # not accessed
    def __init__(self):
        print('ParentA __init__() called.')


class ParentB:
    # not accessed
    def __init__(self):
        print('ParentB __init__() called.')


class Child(ParentA, ParentB):
    def __init__(self):
        print('Child __init__() called.')


# main
child1 = Child()


