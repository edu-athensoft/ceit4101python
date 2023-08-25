"""
module:     shapes
author:     Athensoft Inc.
version:    v1
"""

import shapename as shn
import colorname as color
import math


class Shape:
    def __init__(self, shapeName, shapeType, shapeColor=color.DEFAULT_COLOR):
        self.__shapeName = shapeName
        self.__shapeType = shapeType
        self.__shapeColor = shapeColor

    def getShapeName(self):
        return self.__shapeName

    def getShapeType(self):
        return self.__shapeType

    def setShapeColor(self, color):
        self.__shapeColor = color

    def getShapeColor(self):
        return self.__shapeColor


class Shape2D(Shape):
    def __init__(self, shapeName, shapeType=shn.TYPE_2D):
        super().__init__(shapeName, shapeType)

    def getPerimeter(self):
        print(f"getPerimeter({''}) called.")

    def getArea(self):
        print(f"getArea({''}) called.")


class Shape3D(Shape):
    def __init__(self, shapeName, shapeType=shn.TYPE_3D):
        super().__init__(shapeName, shapeType)

    def getVolume(self):
        print(f"getVolume({''}) called.")

    def getSurfaceArea(self):
        print(f"getSurfaceArea({''}) called.")


class Rectangle(Shape2D):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(shn.RECTANGLE)

    def getPerimeter(self):
        return 2 * (self.a + self.b)

    def getArea(self):
        return self.a * self.b

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},a={self.a},b={self.b}]'


class Square(Shape2D):
    def __init__(self, a):
        self.a = a
        super().__init__(shn.SQUARE)

    def getPerimeter(self):
        return 4 * self.a

    def getArea(self):
        return self.a ** 2

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},a={self.a}]'


class Circle(Shape2D):
    def __init__(self, r):
        self.r = r
        super().__init__(shn.CIRCLE)

    def getPerimeter(self):
        return 2 * math.pi * self.r

    def getArea(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},radius={self.r}]'


class RightTriangle(Shape2D):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(self.a ** 2 + self.b ** 2)
        super().__init__(shn.RIGHT_TRIANGLE)

    def getPerimeter(self):
        return self.a + self.b + self.c

    def getArea(self):
        return self.a * self.b * 0.5

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},a={self.a}, b={self.b}, c(hypotenuse)={self.c}]'


class Sphere(Shape3D):
    def __init__(self, r):
        self.r = r
        super().__init__(shn.SPHERE)

    def getVolume(self):
        return 4 / 3 * math.pi * self.r ** 3

    def getSurfaceArea(self):
        return 4 * math.pi * self.r ** 2

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},r={self.r}]'


class Cube(Shape3D):
    def __init__(self, a):
        self.a = a
        super().__init__(shn.CUBE)

    def getVolume(self):
        return self.a ** 3

    def getSurfaceArea(self):
        return 6 * self.a ** 2

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},a={self.a}]'


class Cylinder(Shape3D):
    def __init__(self, r, h):
        self.r = r
        self.h = h
        super().__init__(shn.CYLINDER)

    def getVolume(self):
        return math.pi * self.r ** 2 * self.h

    def getSurfaceArea(self):
        return math.pi * self.r ** 2 + math.pi * 2 * self.r * self.h

    def __str__(self):
        return f'{__class__.__name__}[shapeType={self.getShapeType()},shapeColor={self.getShapeColor()},radius={self.r},height={self.h}]'
