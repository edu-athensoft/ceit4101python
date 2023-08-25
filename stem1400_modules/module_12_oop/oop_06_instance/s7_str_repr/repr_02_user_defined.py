"""
__str__ method

print out the info of the object

"""

class Cat:
    def __init__(self, name = "NONAME", age=1):
        self.name = name
        self.age = age

    def __repr__(self):
        className = self.__class__.__name__
        return className+"[" \
               +"name='"+self.name+"'," \
               +"age='"+str(self.age)+"'" \
               +"]"

# main
tom = Cat("Tom")

# output the object: tom
print(tom)
print(tom.__repr__())


