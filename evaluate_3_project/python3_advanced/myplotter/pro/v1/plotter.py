"""
Plotter
"""

import shapename as shn


class Plotter:
    @staticmethod
    def fillColor(shapeObj, color):
        print(f"rendering {shapeObj.getShapeName()} in color: {color}")


class Plotter2D(Plotter):
    def __init__(self, shape2dObj):
        self.shapeObj = shape2dObj

    def draw(self):
        print(f"2d drawing {self.shapeObj.getShapeName()}")

    # def fillColor(self, shapeObj, colorName):
    #     print(f"fillColor({shapeObj}{colorName}) called.")


class Plotter3D(Plotter):
    def __init__(self, shape3dObj):
        self.shapeObj = shape3dObj

    # def draw(self, shape3dObj):
    #     print(f"draw({shape3dObj}) called.")

    def draw(self):
        print(f"3d drawing {self.shapeObj.getShapeName()}")

    def fillColor(self, shape3dObj, colorName):
        print(f"fillColor({shape3dObj}{colorName}) called.")


class Plotter2DRectangle(Plotter2D):
    # def draw(self):
    #     print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter2DSquare(Plotter2D):
    # def draw(self):
    #     print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter2DRightTriangle(Plotter2D):
    # def draw(self):
    #     print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter3DSphere(Plotter3D):
    # def draw(self):
    #     print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        print(f'Volume is {self.shapeObj.getVolume():.3f}')


class Plotter3DCube(Plotter3D):
    # def draw(self):
    #     print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        print(f'Volume is {self.shapeObj.getVolume():.3f}')


class Plotter3DCylinder(Plotter3D):
    # def draw(self):
    #     print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        print(f'Volume is {self.shapeObj.getVolume():.3f}')



