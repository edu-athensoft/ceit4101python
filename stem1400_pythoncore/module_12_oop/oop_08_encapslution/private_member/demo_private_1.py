"""
Module 12. OOP

private members
private attributes
"""

class Duck:
    def __init__(self, name):
        self.name = name
        self.__age = 2      # by month

# main
duck1 = Duck("Peter")

# public attribute
print(duck1.name)

# AttributeError: 'Duck' object has no attribute '__age'
# print(duck1.__age)


