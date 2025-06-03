"""
31. Is it possible to safely check if a class/object has a certain attribute?

A. yes, by using the hasattr attribute
B. yes, by using the hasattr ( ) method
C. yes, by using the hassattr ( ) function
D. no, it is not possible

"""

class Car:
    def __init__(self):
        self.model = "BMW X320"
        self.max_speed = 180


mycar = Car()

result = hasattr(mycar, "max_speed")
print(result)

result = hasattr(mycar, "width")
print(result)
