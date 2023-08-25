"""
test plotter
"""

from shapes import *
from plotter import *


# test drawing 2d shapes
print("=== test Rectangle ===")
shape1 = Rectangle(3,4)
plotter1 = Plotter2DRectangle(shape1)
plotter1.draw()
print()

# test drawing 2d shapes
print("=== test Square ===")
shape2 = Square(3)
plotter2 = Plotter2DSquare(shape2)
plotter2.draw()
print()

# test drawing 3d shapes
print("=== test Sphere ===")
shape3 = Sphere(1)
plotter3 = Plotter3DSphere(shape3)
plotter3.draw()
print()

# test drawing 3d shapes
print("=== test Cube ===")
shape4 = Cube(2)
plotter4 = Plotter3DCube(shape4)
plotter4.draw()
print()

