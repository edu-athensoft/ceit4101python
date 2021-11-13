"""
Accessing instance members

updating and accessing an instance attribute
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
cat1 = Cat('Tom','orange')

# directly accessing
# however it is not recommended
cat1_name = cat1.name

print(f'The attribute cat1.name is: {cat1_name}')
print()

# now it is changed externally
# however it is not recommended
cat1.name = 'Jack'
cat1_name = cat1.name

print(f'cat1.name was just changed.')
print(f'The attribute cat1.name is: {cat1_name}')



