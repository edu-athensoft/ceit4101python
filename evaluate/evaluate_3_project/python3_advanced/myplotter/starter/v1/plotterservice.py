"""

"""

from plotter import *
import shapename as shn


class PlotterService:

    def plot(self, shapeObj):
        shapeType = shapeObj.getShapeType()
        # print(f'>>> shapeType={shapeType}')

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
