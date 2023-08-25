"""
Plotter
- general plotter (renderer)
- 2d plotter
- 3d plotter
"""

import shapename as shn

class Plotter:
    def __init__(self, shapeObj):
        self.shapeObj = shapeObj

    def draw(self):
        pass

    def fillColor(self, color):
        print(f"rendering {self.shapeObj.getShapeName()} in color: {color}")
        self.shapeObj.setShapeColor(color)


class Plotter2D(Plotter):
    # def __init__(self, shape2dObj):
    #     self.shapeObj = shape2dObj

    def draw(self):
        print(f"2d drawing {self.shapeObj.getShapeName()}")

    def printPerimeter(self):
        print(f'Perimeter is {self.shapeObj.getPerimeter()}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea()}')


class Plotter3D(Plotter):
    # def __init__(self, shape3dObj):
    #     self.shapeObj = shape3dObj

    def draw(self):
        print(f"3d drawing {self.shapeObj.getShapeName()}")

    def printSurfaceArea(self):
        print(f'SurfaceArea is {self.shapeObj.getSurfaceArea():.3f}')

    def printVolume(self):
        self.x = print(f'Volume is {self.shapeObj.getVolume():.3f}')


class Plotter2DRectangle(Plotter2D):
    pass

class Plotter2DSquare(Plotter2D):
    pass

class Plotter2DCircle(Plotter2D):
    pass

class Plotter2DRightTriangle(Plotter2D):
    pass

class Plotter3DSphere(Plotter3D):
    pass

class Plotter3DCube(Plotter3D):
    pass

class Plotter3DCylinder(Plotter3D):
    pass

class PlotterFactory:
    @staticmethod
    def getPlotterByType(shapeObj):
        shapeType = shapeObj.getShapeType()

        if shapeType == shn.TYPE_2D:
            plotterObj = Plotter2D(shapeObj)
        elif shapeType == shn.TYPE_3D:
            plotterObj = Plotter3D(shapeObj)
        else:
            print('[Error]Invalid shape')
        return plotterObj

    @staticmethod
    def getPlotterByName(shapeObj):
        plotterObj = None
        shapeName = shapeObj.getShapeName()
        if shapeName == shn.RECTANGLE:
            plotterObj = Plotter2DRectangle(shapeObj)
        if shapeName == shn.SQUARE:
            plotterObj = Plotter2DSquare(shapeObj)
        if shapeName == shn.RIGHT_TRIANGLE:
            plotterObj = Plotter2DRightTriangle(shapeObj)
        if shapeName == shn.SPHERE:
            plotterObj = Plotter3DSphere(shapeObj)
        if shapeName == shn.CUBE:
            plotterObj = Plotter3DCube(shapeObj)
        if shapeName == shn.CYLINDER:
            plotterObj = Plotter3DCylinder(shapeObj)
        return plotterObj

    @staticmethod
    def getPlotter(shapeObj):
        return Plotter(shapeObj)