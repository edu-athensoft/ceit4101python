"""
multiple init

child has its own init() method
child has its own property: gender
child has its own property: name
parent has a property: name (does not take effect)

by MRO rules,
child called its own init() method
"""


class ParentA:
    # not accessed
    # the property name is not visible
    def __init__(self, name):
        print('ParentA __init__() called.')
        self.name = name


class ParentB:
    # not accessed
    def __init__(self):
        print('ParentB __init__() called.')


class Child(ParentA, ParentB):
    def __init__(self, gender, name):
        print('Child __init__() called.')
        self.gender = gender
        self.name = name + ' at Child'


# main
child1 = Child('Male', 'Peter')
print(child1.gender)
print(child1.name)

