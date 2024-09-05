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
# however it is not recommended
cat1_name = cat1.name

print(f'The attribute cat1.name is: {cat1_name}')
