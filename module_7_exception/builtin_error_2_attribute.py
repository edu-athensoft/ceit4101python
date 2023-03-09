"""
built-in error
AttributeError
"""

class MyCar:
    def __init__(self):
        self.id = 1
        self.brand = "BMW"
        self.price = 50000


car1 = MyCar()
print(car1.brand)

print(car1.width)
# AttributeError: 'MyCar' object has no attribute 'width'

# car1.width = 2.2
# print(car1.width)
