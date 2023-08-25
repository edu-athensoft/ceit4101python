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

    def get_age(self):
        return self.__age

    def get_secret(self):
        self.__secret()

# main
duck1 = Duck("Peter")

# directly access private members
# Do not write this way in your program
print(duck1._Duck__age)
duck1._Duck__secret()


