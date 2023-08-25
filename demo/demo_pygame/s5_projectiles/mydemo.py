"""
test projectile
"""

# class projectile(object):
#     def __int__(self, x, y, radius, color, facing):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color
#         self.facing = facing
#         self.vel = 8 * facing


# main program
# a = projectile(1,2,3,4,5)


class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Cat(1,2)
print(a, type(a))