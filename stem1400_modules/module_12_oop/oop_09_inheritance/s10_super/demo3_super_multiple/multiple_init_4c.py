"""
multiple init

child inherits properties from different classes.
child has its own init() method
child has its own property: gender
child inherits property of ParentB: name
ParentB has a property: name
child inherits property of ParentA: age
ParentB has a property: age

passing *args

by MRO rules,
child called its own init() method
child called ParentB init()


"""


class ParentA:
    def __init__(self, age, *args):
        print('ParentA __init__() called.')
        self.age = str(age) + ' at ParentA'
        # IMPORTANT
        # using super() to continue to call ParentB.__init__()
        super().__init__(*args)


class ParentB:
    def __init__(self, name, *args):
        print('ParentB __init__() called.')
        self.name = name + ' at ParentB'


class Child(ParentA, ParentB):
    def __init__(self, gender, name, age):
        print('Child __init__() called.')
        self.gender = gender
        super().__init__(age, name)


# main
print(Child.__mro__)

child1 = Child('gender:Male', 'name:Peter', 16)
print(child1.gender)
print(child1.name)
print(child1.age)



