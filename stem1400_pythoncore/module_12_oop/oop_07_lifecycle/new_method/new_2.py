"""
overriding __new__()

correctly
returning instance references which leads to success in initializing
"""


class Cat:
    def __new__(cls):
        print('__new__() is called.')
        return super().__new__(cls)

    def __new__(cls, *args, **kwargs):
        print('__new__() is called.')
        return super().__new__(cls)

    def __init__(self):
        print('__init_() is called.')


# main program
tom = Cat()

# output None because it was not really instantiated
print(tom)
