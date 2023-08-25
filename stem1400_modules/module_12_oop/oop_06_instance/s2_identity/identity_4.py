"""
instance or object of a class
identity
id()
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
tom = Cat('Tom',1)
peter = Cat('Tom',1)
jack = Cat('Tom',1)

print(id(tom))
print(id(peter))
print(id(jack))

# 24835472
# 24835504
# 24835536
print("=====")
tomma = tom

# question
# are they identical?
print(id(tomma))
print(id(tom))
# 34010576
# 34010576





