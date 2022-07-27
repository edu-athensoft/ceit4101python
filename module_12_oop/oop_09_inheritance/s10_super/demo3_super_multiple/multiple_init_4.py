"""
multiple init

child has its own init() method
child has its own property: gender
child inherits property of ParentB: name
ParentB has a property: name
ParentA has no attribute: name

by MRO rules,
child called its own init() method
child called ParentB init()
"""


class ParentA:
    def __init__(self, age):
        print('ParentA __init__() called.')
        self.age = str(age) + ' at ParentA'


class ParentB:
    # accessed under MRO
    def __init__(self, name):
        print('ParentB __init__() called.')
        self.name = name + ' at ParentB'


class Child(ParentA, ParentB):
    def __init__(self, gender, name):
        print('Child __init__() called.')
        self.gender = gender

        # ParentA has no attribute: name
        super().__init__(name)


# main
child1 = Child('gender:Male', 'name:Peter')
print(child1.gender)


print(child1.name)
# AttributeError: 'Child' object has no attribute 'name'

print(child1.age)
# not reached


