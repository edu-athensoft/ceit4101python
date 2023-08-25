"""
__init__ method

defining instance attributes within init method
as well as giving default value

passing value for attribute when creating objects

self.attrName = initValue

"""

class Cat:

    def __init__(self, _name = "NONAME"):
        print("__init__ method")

        # register an attribute
        # self.name = 'NoName'

        self.name = _name


# main
# passing value and set attribute
tom = Cat("Tom")

# accessing an instance variable/attribute
print(tom.name)


peter = Cat()

# accessing an instance variable/attribute
print(peter.name)


