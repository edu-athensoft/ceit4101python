"""
client app
start edition
"""

from shapes import *
from plotterservice import *


def main():
    print("=== My Plotter App ===")
    print("=== Starter edition ===")
    print()

    # init
    ps = PlotterService()

    # plot a rectangle
    shape1 = Rectangle(3,4)
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

    print()

    # plot a cube
    shape4 = Cube(2)
    print(shape4)
    ps.plot(shape4)


if __name__ == '__main__':
    main()
