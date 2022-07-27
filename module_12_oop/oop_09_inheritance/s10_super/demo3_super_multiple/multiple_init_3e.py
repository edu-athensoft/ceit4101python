"""
multiple init

child has its own init() method
child has its own property: gender
child inherits property of ParentB: name
ParentA has no init()
ParentB has a property: name

by MRO rules,
child called its own init() method
child called ParentB init()


"""


class ParentA:
    # def __init__(self, name):
    #     print('ParentA __init__() called.')
    #     self.name = name + ' at ParentA'
    pass


class ParentB:
    # accessed under MRO
    def __init__(self, name):
        print('ParentB __init__() called.')
        self.name = name + ' at ParentB'


class Child(ParentA, ParentB):
    def __init__(self, gender, name):
        print('Child __init__() called.')
        self.gender = gender
        super().__init__(name)


# main
child1 = Child('Male', 'Peter')
print(child1.gender)
print(child1.name)

