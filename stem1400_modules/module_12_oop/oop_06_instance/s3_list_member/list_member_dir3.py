"""
list all members
dir(target_object)

where target_object can be literal or a variable name

"""


class Duck:
    # define instance attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color


# main program
duck1 = Duck('Jack', 'white')
results = dir(duck1)

for member in results:
    print(member)

