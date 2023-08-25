"""
shape service
"""


class ShapeFactory:
    @staticmethod
    def getShapeByName(shapeName, **param):
        shapeNameWords = shapeName.strip().split()
        shapeName = ''
        for word in shapeNameWords:
            shapeName += word.title()
        shapeObj = eval(shapeName)(**param)
        return shapeObj
