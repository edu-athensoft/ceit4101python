"""
Plotter
"""

import shapename as shn


class Plotter:
    pass


class Plotter2D(Plotter):
    def __init__(self, shape2dObj):
        self.shapeObj = shape2dObj

    # def draw(self, shape2dObj):
    #     print(f"draw({shape2dObj}) called.")

    # def fillColor(self, shapeObj, colorName):
    #     print(f"fillColor({shapeObj}{colorName}) called.")


class Plotter3D(Plotter):
    def __init__(self, shape3dObj):
        self.shapeObj = shape3dObj

    def draw(self, shape3dObj):
        print(f"draw({shape3dObj}) called.")

    def fillColor(self, shape3dObj, colorName):
        print(f"fillColor({shape3dObj}{colorName}) called.")


class Plotter2DRectangle(Plotter2D):
    def draw(self):
        print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter2DSquare(Plotter2D):
    def draw(self):
        print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter3DSphere(Plotter3D):
    def draw(self):
        print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        print(f'Volume is {self.shapeObj.getVolume():.3f}')


class Plotter3DCube(Plotter3D):
    def draw(self):
        print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        print(f'Volume is {self.shapeObj.getVolume():.3f}')


class PlotterFactory:
    @staticmethod
    def getPlotter(shapeObj):
        plotterObj = None
        shapeName = shapeObj.getShapeName()
        # print(f'>>> shapeName = {shapeName}')
        if shapeName == shn.RECTANGLE:
            plotterObj = Plotter2DRectangle(shapeObj)
        if shapeName == shn.SQUARE:
            plotterObj = Plotter2DSquare(shapeObj)
        if shapeName == shn.SPHERE:
            plotterObj = Plotter3DSphere(shapeObj)
        if shapeName == shn.CUBE:
            plotterObj = Plotter3DCube(shapeObj)
        return plotterObj
