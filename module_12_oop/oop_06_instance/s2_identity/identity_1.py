"""
Identity of objects
built-in method: id()
"""


class Duck:
    pass


# main program
duck1 = Duck()

print(f'object id = {id(duck1)}')
