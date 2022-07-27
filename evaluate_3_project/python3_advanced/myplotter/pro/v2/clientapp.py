"""
Client app
pro edition
"""

from colorname import *
from shapes import *
from plotterservice import *


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
    print(shape1)
    print()

    # plot a square
    shape2 = Square(5)
    print(shape2)
    ps.plot(shape2)
    ps.fill_color(shape2, COLOR_GREEN)
    print(shape2)
    print()

    # plot a sphere
    shape3 = Sphere(6)
    print(shape3)
    ps.plot(shape3)
    ps.fill_color(shape3, COLOR_GREEN)
    print(shape3)
    print()

    # plot a cube
    shape4 = Cube(2)
    print(shape4)
    ps.plot(shape4)
    ps.fill_color(shape4, COLOR_RED)
    print()

    # plot a right triangle
    shape5 = RightTriangle(3, 4)
    print(shape5)
    ps.plot(shape5)
    ps.fill_color(shape5, COLOR_BLUE)
    print(shape5)
    print()

    # plot a cylinder
    shape6 = Cylinder(2, 3)
    print(shape6)
    ps.plot(shape6)
    ps.fill_color(shape6, COLOR_YELLOW)
    print(shape6)
    print()

    # plot a circle
    shape7 = Circle(1)
    print(shape7)
    ps.plot(shape7)
    ps.fill_color(shape7, COLOR_YELLOW)
    print(shape7)
    print()

if __name__ == '__main__':
    main()
