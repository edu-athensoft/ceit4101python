"""
Accessing instance members

Accessing an instance attribute
"""


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print("I eat.")

    def sleep(self):
        print("I sleep.")


# main program
# creating an object of Cat class
cat1 = Cat('Tom', 'orange')

# directly accessing
cat1.eat()
cat1.sleep()
