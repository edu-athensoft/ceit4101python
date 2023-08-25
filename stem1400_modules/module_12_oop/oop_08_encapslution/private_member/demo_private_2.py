"""
Module 12. OOP

private members
private method
"""

class Duck:
    def __init__(self, name):
        self.name = name
        self.__age = 2      # by month

    def __secret(self):
        print("private method: __secret() is called.")
        print(f"private __age = {self.__age} can be accessed through private methods.")

    def get_age(self):
        # print(f"age = {self.__age}")
        return self.__age

    def get_secret(self):
        self.__secret()

# main
duck1 = Duck("Peter")

# AttributeError: 'Duck' object has no attribute '__age'
# print(duck1.__age)

# AttributeError: 'Duck' object has no attribute '__secret'
# duck1.__secret()

age = duck1.get_age()
print(f"private __age = {age} can be accessed through public methods.")
print()

duck1.get_secret()

