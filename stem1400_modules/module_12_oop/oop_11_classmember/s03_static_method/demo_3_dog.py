"""
example of static method

unnecessary instance method
"""


class Dog:

    # why there is a warning sign?
    # the method may be static
    # because self is not used
    def run(self):
        print("A dog runs.")
