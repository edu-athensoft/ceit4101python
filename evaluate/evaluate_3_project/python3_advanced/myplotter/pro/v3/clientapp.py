"""
Client app
pro edition
"""
from shapename import *
from colorname import *
from shapeservice import *
from plotterservice import *


def main():
    print("=== My Plotter App ===")
    print("=== Professional edition ===")
    print()

    # init
    ps = PlotterService()

    # plot a rectangle
    shape1 = ShapeFactory.getShapeByName(RECTANGLE, width=1, height=2)
    print(shape1)
    ps.plot(shape1)
    print(shape1)
    print()

    # plot a square
    shape2 = ShapeFactory.getShapeByName(SQUARE, a=1)
    print(shape2)
    ps.plot(shape2)
    ps.fill_color(shape2, COLOR_GREEN)
    print(shape2)
    print()

    # plot a sphere
    shape3 = ShapeFactory.getShapeByName(SPHERE, r=1)
    print(shape3)
    ps.plot(shape3)
    ps.fill_color(shape3, COLOR_GREEN)
    print(shape3)
    print()

    # plot a cube
    shape4 = ShapeFactory.getShapeByName(CUBE, a=1)
    print(shape4)
    ps.plot(shape4)
    ps.fill_color(shape4, COLOR_RED)
    print()

    # plot a right triangle
    shape5 = ShapeFactory.getShapeByName(RIGHT_TRIANGLE, a=3, b=4)
    print(shape5)
    ps.plot(shape5)
    ps.fill_color(shape5, COLOR_BLUE)
    print(shape5)
    print()

    # plot a cylinder
    shape6 = ShapeFactory.getShapeByName(CYLINDER, r=1, h=1)
    print(shape6)
    ps.plot(shape6)
    ps.fill_color(shape6, COLOR_YELLOW)
    print(shape6)
    print()

    # plot a circle
    shape7 = ShapeFactory.getShapeByName(CIRCLE, r=1)
    print(shape7)
    ps.plot(shape7)
    ps.fill_color(shape7, COLOR_YELLOW)
    print(shape7)
    print()


if __name__ == '__main__':
    main()
