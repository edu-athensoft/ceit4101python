"""
__del__ method
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
# passing value and set attribute
tom = Cat("Tom")

# accessing an instance variable/attribute
print(tom.name)

#
print("program end.")


# output
# pay attention to the last line
# the tom object was collected as garbage after main program finished.

"""
__init__ method
Tom
program end.
__del__ method is called
"""
