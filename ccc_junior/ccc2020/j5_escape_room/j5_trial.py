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

map = []
# map.append((1,1))
# map.append((1,2))
# map.append((1,3))
# map.append((1,4))
#
# map.append((2,1))
# map.append((2,2))
# map.append((2,3))
# map.append((2,4))
#
# map.append((3,1))
# map.append((3,2))
# map.append((3,3))
# map.append((3,4))

# cell = tuple(cell)
# map = tuple(map)

cells_dict = dict(cells)
map = tuple(cells_dict)

print(cells)
print(cells_dict)

print(map)

def getCordinate(num):
    coords = []
    for i in range(1, num+1):
        if num % i ==0:
            x = int(num / i)
            y = i
            coords.append((x,y))
    return tuple(coords)

def getLastCells(cell):
    value_thiscell = cell[1]
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
cell = ((3, 4), 9)
# print(getLastCells(cell))
path.append(cell)

result = 'no'

def getPath(cell):
    global result
    while True:
        lastcells = getLastCells(cell)
        if len(lastcells) > 0:
            path.extend(lastcells)
            for lastcell in lastcells:
                print(lastcell)
                cell = lastcell
                if lastcell[0] == (1,1):
                    # break
                    result = 'yes'
                    # return result
                    return
getPath(cell)
print(result)




