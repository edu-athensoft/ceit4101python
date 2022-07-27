"""

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

    def __plot2d(self, shapeObj):
        # get plotter object
        plotter = PlotterFactory.getPlotter(shapeObj)
        plotter.draw()
        plotter.printPerimeter()
        plotter.printArea()

    def __plot3d(self, shapeObj):
        # get plotter object
        plotter = PlotterFactory.getPlotter(shapeObj)
        plotter.draw()
        plotter.printSurfaceArea()
        plotter.printVolume()


class PlotterFactory:
    @staticmethod
    def getPlotter(shapeObj):
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
