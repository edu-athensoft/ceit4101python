"""

"""

cells = []
cells.append(((1,1),3))
cells.append(((1,2),10))
cells.append(((1,3),8))
cells.append(((1,4),14))

cells.append(((2,1),1))
cells.append(((2,2),11))
cells.append(((2,3),12))
cells.append(((2,4),12))

cells.append(((3,1),6))
cells.append(((3,2),2))
cells.append(((3,3),3))
cells.append(((3,4),9))

print(cells)

cells_dict = dict(cells)
print(cells_dict)

map = tuple(cells_dict)
print(map)


def getNeighborCells(cell):
    # value_thiscell = cell[1]
    # search for neighbors
    neighbor_cells = []
    value_lastcell = cell[0][0] * cell[0][1]
    for cell in cells:
        if cell[1] == value_lastcell:
            # print(cell)
            neighbor_cells.append(cell)
    # return value_lastcell
    return neighbor_cells


# main
print("===============")
path = []
exit_cell = ((3, 4), 9)
path.append(exit_cell)

result = 'no'

def getPath(cell):
    pass


class Cell:
    def __init__(self,cell):
        self.cell = cell
        self.cellcoord = cell[0]
        self.cellvalue = cell[1]
        self.children = []

    def addChild(self,cell):
        self.children.append(cell)

    def getNextCells(self):
        coords = self.getCoordinates(self.cellvalue, 3, 4)
        nextCells = []
        for coord in coords:
            print("coord=",coord)
            nextCells.append((coord,cells_dict[coord]))
        return nextCells

    def hasNext(self):
        if not self.children:
            return True
        else:
            return False

    def hasChildren(self):
        if len(self.children) == 0:
            return False
        else:
            return True

    def getCoordinates(self, cell_value, Mrow, Ncol):
        coords = []
        for i in range(1, cell_value+1):
            if cell_value % i ==0:
                x = int(cell_value / i)
                y = i
                if y<= Ncol and x<=Mrow:
                    coords.append((x,y))
        return tuple(coords)

    def __repr__(self):
        return f"({self.cell})"

    def printChildren(self):
        for item in self.children:
            print(item)


class Path:
    def __init__(self,root):
        self.root = root
        self.path = [self.root]
        self.cells = cells

    def createPath(self, currentCell):
        while currentCell.hasNext():
            nextCells = currentCell.getNextCells()
            # for nextCell in nextCells:
            #     currentCell.addChild(nextCell)
            while len(nextCells) >0:
                nextCell = Cell(nextCells.pop())
                print("nextCell=",nextCell)
                currentCell.addChild(nextCell)
                self.createPath(nextCell)

    def getPaths(self):
        cell = self.root
        while cell.hasChildren():
            cell.printChildren()



root = Cell(((1, 1), 3))
# print(root.getNextCells(root, cells))

path = Path(root)
path.createPath(root)
path.getPaths()




