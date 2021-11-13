"""
__str__ method

print out object directly
without defining __str__()

"""

class Cat:
    def __init__(self, _name = "NONAME"):
        self.name = _name

# main
tom = Cat("Tom")

# output the object: tom
print(tom)


