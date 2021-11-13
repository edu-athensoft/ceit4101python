"""
__del__ method

keyword: del
delete an object and call __del__ method at once.
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

# delete an object
del tom

#
print("program end.")


# output
# pay attention to the last line
# the tom object was collected as garbage when executing del statement

"""
__init__ method
Tom
__del__ method is called
program end.
"""
