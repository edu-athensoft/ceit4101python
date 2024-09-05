"""
super and init

child overrides init() of parent and use its own init()

child has its own property: age
parent has a property: name

child cannot inherit parent's property due to overriding,
properties defined in parent do not take effect to child.
"""


class Parent:
    def __init__(self, name):
        print('Parent __init__() called.')
        self.name = name


class Child(Parent):
    def __init__(self, age):
        print('Child __init__() called.')
        self.age = age


# main
# c1 = Child()
# TypeError: __init__() missing 1 required positional argument: 'age'

c1 = Child(16)
print(c1.age)

# print(c1.name)
# AttributeError: 'Child' object has no attribute 'name'
# there is no such attribute defined in Child


