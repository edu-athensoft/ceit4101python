"""
example of static method

static method
"""


class Dog:
    @staticmethod
    def run():
        # no need to use 'self'
        print("A dog runs.")


# main
Dog.run()
Dog.run()
