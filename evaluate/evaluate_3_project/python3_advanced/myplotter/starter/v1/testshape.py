"""
Test App
version:    v1
"""

from shapes import *
from shapename import *

# test Shape
print("=== test Shape ===")
myshape1 = Shape()
# myshape1.draw("rectangle")
# myshape1.fillColor("red")
print()

# test Shape2D
print("=== test Shape2D ===")
myshape21 = Shape2D()
# myshape21.draw("rectangle")
# myshape21.fillColor("red")
myshape21.getPerimeter()
myshape21.getArea()
print()

# test Shape3D
print("=== test Shape3D ===")
myshape31 = Shape3D()
# myshape31.draw("rectangle")
# myshape31.fillColor("red")
myshape31.getSurfaceArea()
myshape31.getVolume()
print()

# test creating objects
# print("=== test ShapeFactory ===")
# rectangle1 = ShapeFactory.create2DShape(RECTANGLE)
# square1 = ShapeFactory.create2DShape(SQUARE)
# sphere1 = ShapeFactory.create3DShape(SPHERE)
# cube1 = ShapeFactory.create3DShape(CUBE)
# print(rectangle1)
# print(square1)
# print(sphere1)
# print(cube1)

# test 2d shapes
print("=== test Rectangle ===")
sp1 = Rectangle(3, 4)
# sp1.draw(RECTANGLE)
# sp1.fillColor("RED")
sp1.getArea()
sp1.getPerimeter()
print()

print("=== test Square ===")
sp2 = Square(5)
# sp2.draw()
# sp2.fillColor("RED")
sp2.getArea()
sp2.getPerimeter()
print()

# test 3d shapes
print("=== test Sphere ===")
sp3 = Sphere(1)
# sp3.draw()
# sp3.fillColor("RED")
sp3.getSurfaceArea()
sp3.getVolume()

print("=== test Cube ===")
sp4 = Cube(3)
# sp4.draw()
# sp4.fillColor("RED")
sp4.getSurfaceArea()
sp4.getVolume()



