"""
__str__ method

print out the info of the object

"""

class Cat:

    def __init__(self, _name = "NONAME"):
        print("__init__ method")

        # register an attribute
        # self.name = 'NoName'

        self.name = _name


    def __del__(self):
        print("__del__ method is called")



# main
tom = Cat("Tom")

# output the object: tom
print(tom)

#
print("program end.")

