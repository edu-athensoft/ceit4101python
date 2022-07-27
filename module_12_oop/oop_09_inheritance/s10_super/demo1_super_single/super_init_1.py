"""
super and init

child directly inherits init() of parent
no properties
"""


class Parent:
    def __init__(self):
        print('Parent __init__() called.')


class Child(Parent):
    pass


# main
c1 = Child()





