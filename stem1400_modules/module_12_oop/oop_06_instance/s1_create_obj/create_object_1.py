"""
defining a class
adding attributes and methods

__init__():  built-in method

"""

class Cat:
    def __int__(self, name, color, size, age):
        self.name = name
        self.color = color
        self.size = size
        self.age = age

    def sleep(self):
        pass

    def meow(self):
        pass

    def run(self):
        pass

    def jump(self):
        pass


# main program
tom = Cat()
# tom = 1
print(tom)