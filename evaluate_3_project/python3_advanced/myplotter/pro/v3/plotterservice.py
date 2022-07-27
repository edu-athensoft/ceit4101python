"""
PlotterService
- plot shape (by type, by name)
- fill color
"""

from plotter import *
import shapename as shn


class PlotterService:
    def plot(self, shapeObj):
        shapeType = shapeObj.getShapeType()

        print(f"starting plotting...")
        if shapeType == shn.TYPE_2D:
            self.__plot2d(shapeObj)
        elif shapeType == shn.TYPE_3D:
            self.__plot3d(shapeObj)
        else:
            print('[Error]Invalid shape')
        print(f"plotted.")

    def fill_color(self, shapeObj, colorName):
        print(f"rendering shape...")
        plotter = PlotterFactory.getPlotter(shapeObj)
        # plotter.fillColor(shapeObj, colorName)
        plotter.fillColor(colorName)
        print(f"color filled.")

    def __plot2d(self, shapeObj):
        # get plotter object
        plotter = PlotterFactory.getPlotterByType(shapeObj)
        plotter.draw()
        plotter.printPerimeter()
        plotter.printArea()

    def __plot3d(self, shapeObj):
        # get plotter object
        plotter = PlotterFactory.getPlotterByType(shapeObj)
        plotter.draw()
        plotter.printSurfaceArea()
        plotter.printVolume()


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
