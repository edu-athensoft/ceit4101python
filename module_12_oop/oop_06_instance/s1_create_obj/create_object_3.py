"""
instance or object of a class
"""

# defining a class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('sleep() is called')

    def eat(self):
        print('eat() is called')


# main program
# creating multiple instances
# 3 objects(instances)
# tom = Cat('Tom',1)
# peter = Cat('Peter',2)
# jack = Cat('Jack',3)

tom = Cat('Tom',1)
peter = Cat('Tom',1)
jack = Cat('Tom',1)

print("=====")

tom = Cat('Tom',1)
tom2 = Cat('Tom',1)
tom3 = Cat('Tom',1)

# question
# are they (tom, tom2, tom3) identical objects?






