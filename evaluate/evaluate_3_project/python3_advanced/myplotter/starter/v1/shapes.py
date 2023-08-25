"""
module:     shapes
author:     Athensoft Inc.
version:    v1
"""

import shapename as shn
import math


class Shape:
    def __init__(self, shapeName, shapeType):
        self.__shapeName = shapeName
        self.__shapeType = shapeType

    def getShapeName(self):
        return self.__shapeName

    def getShapeType(self):
        return self.__shapeType


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
        result = 2 * (self.a + self.b)
        # print(f"Perimeter = {result}")
        return result

    def getArea(self):
        result = self.a * self.b
        # print(f"Area = {result}")
        return result

    def __str__(self):
        return f'{__class__.__name__}[a={self.a},b={self.b}]'


class Square(Shape2D):
    def __init__(self, a):
        self.a = a
        super().__init__(shn.SQUARE)

    def getPerimeter(self):
        result = 4 * self.a
        # print(f"Perimeter = {result}")
        return result

    def getArea(self):
        result = self.a ** 2
        # print(f"Area = {result}")
        return result

    def __str__(self):
        return f'{__class__.__name__}[a={self.a}]'


class Sphere(Shape3D):
    def __init__(self, r):
        self.r = r
        super().__init__(shn.SPHERE)

    def getVolume(self):
        result = 4 / 3 * math.pi * self.r ** 3
        # print(f"Volume = {result}")
        return result

    def getSurfaceArea(self):
        result = 4 * math.pi * self.r ** 2
        # print(f"SurfaceArea = {result}")
        return result

    def __str__(self):
        return f'{__class__.__name__}[r={self.r}]'


class Cube(Shape3D):
    def __init__(self, a):
        self.a = a
        super().__init__(shn.CUBE)

    def getVolume(self):
        result = self.a ** 3
        # print(f"Volume = {result}")
        return result

    def getSurfaceArea(self):
        result = 6 * self.a ** 2
        # print(f"SurfaceArea = {result}")
        return result

    def __str__(self):
        return f'{__class__.__name__}[a={self.a}]'


"""
class ShapeFactory:
    @staticmethod
    def create2DShape(shapeName):
        shape2dObj = Shape2D()
        if shapeName == shn.RECTANGLE:
            shape2dObj = Rectangle()
        if shapeName == shn.SQUARE:
            shape2dObj = Square()
        return shape2dObj

    @staticmethod
    def create3DShape(shapeName):
        shape3dObj = Shape3D()
        if shapeName == shn.SPHERE:
            shape3dObj = Sphere()
        if shapeName == shn.CUBE:
            shape3dObj = Cube()
        return shape3dObj
"""
