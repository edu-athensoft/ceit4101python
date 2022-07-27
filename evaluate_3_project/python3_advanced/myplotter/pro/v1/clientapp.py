"""
client app
pro edition
"""

from shapes import *
from plotterservice import *
from colorname import *


def main():
    print("=== My Plotter App ===")
    print("=== Professional edition ===")
    print()

    # init
    ps = PlotterService()

    # plot a rectangle
    shape1 = Rectangle(3, 4)
    print(shape1)
    ps.plot(shape1)

    print()

    # plot a square
    shape2 = Square(5)
    print(shape2)
    ps.plot(shape2)

    print()

    # plot a sphere
    shape3 = Sphere(6)
    print(shape3)
    ps.plot(shape3)
    Plotter.fillColor(shape3, COLOR_GREEN)

    print()

    # plot a cube
    shape4 = Cube(2)
    print(shape4)
    ps.plot(shape4)
    Plotter.fillColor(shape4, COLOR_RED)

    print()

    # plot a right triangle
    shape5 = RightTriangle(3, 4)
    print(shape5)
    ps.plot(shape5)
    Plotter.fillColor(shape5, COLOR_BLUE)

    print()

    # plot a cylinder
    shape6 = Cylinder(2, 3)
    print(shape6)
    ps.plot(shape6)
    Plotter.fillColor(shape6, COLOR_YELLOW)


if __name__ == '__main__':
    main()
