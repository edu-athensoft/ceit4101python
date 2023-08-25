"""
__init__ method

defining instance attributes within init method

self.attrName = initValue
"""

class Cat:

    def __init__(self):
        print("__init__ method")

        # register an attribute
        self.name = 'NoName'


# main
tom = Cat()

# accessing an instance variable/attribute
print(tom.name)


