"""
overriding __new__()

error
without returning instance references which results in failure of initializing
"""


class Cat:
    def __new__(cls):
        print('__new__() is called.')

    def __init__(self):
        print('__init_() is called.')

# main program
tom = Cat()

# output None because it was not really instantiated
print(tom)
