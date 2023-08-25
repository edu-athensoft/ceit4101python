"""
Plotter
- general plotter (renderer)
- 2d plotter
- 3d plotter
"""


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
        print(f'Perimeter is {self.shapeObj.getPerimeter():.3f}')

    def printArea(self):
        print(f'Area is {self.shapeObj.getArea():.3f}')

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


