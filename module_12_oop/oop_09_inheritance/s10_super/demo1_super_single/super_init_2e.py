"""
super and init

child overrides init() of parent and use its own init()

child has its own property: age
parent has a property: name

child inherit parent's property by super(),
child init() must accept all parameters

the order of parameter matters
"""


class Parent:
    def __init__(self, name):
        print('Parent __init__() called.')
        self.name = name


class Child2(Parent):
    def __init__(self, age, name):
        print('Child __init__() called.')
        self.age = age
        super().__init__(name)


# main
# order of arguments do not match that of the declared parameters
c2 = Child2('Jack', 18)
print('age:',c2.age)
print('name:',c2.name)


