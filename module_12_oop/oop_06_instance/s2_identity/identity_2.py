"""
Identity of objects
built-in method: id()
"""


class Duck:
    pass


# main program
duck1 = Duck()
duck2 = Duck()

print(f'object1 id = {id(duck1)}')
print(f'object2 id = {id(duck2)}')
