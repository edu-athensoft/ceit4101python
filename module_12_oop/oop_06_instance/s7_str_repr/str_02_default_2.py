"""
__str__ method

print out the info of the object

"""

class Cat:
    def __init__(self, _name = "NONAME"):
        self.name = _name

# main
tom = Cat("Tom")

# output the object: tom
print(tom)
print(tom.__str__())


