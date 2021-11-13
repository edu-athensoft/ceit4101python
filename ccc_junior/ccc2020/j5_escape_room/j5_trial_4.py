"""

3 10 8 14
1 11 12 12
6 2 3 9

"""


# input
# row
M = int(input())
# column
N = int(input())

# cells
cells = []
for m in range(M):
    line = input().split()
    for n, x in enumerate(line):
        cells.append(((m+1,n+1),int(x)))

cells_dict = dict(cells)

def getLastCells(cell):
    # value_thiscell = cell[1]
    # search for neighbors
    neighbor_cells = []
    value_lastcell = cell[0][0] * cell[0][1]
    for cell in cells:
        if cell[1] == value_lastcell:
            neighbor_cells.append(cell)
    return neighbor_cells


# main
path = []
cell = ((3, 4), 9)
path.append(cell)
result = 'no'

def getPath(cell):
    global result
    while True:
        lastcells = getLastCells(cell)
        if len(lastcells) > 0:
            path.extend(lastcells)
            for lastcell in lastcells:
                # print(lastcell)
                cell = lastcell
                if lastcell[0] == (1,1):
                    # break
                    result = 'yes'
                    # return result
                    return
getPath(cell)
print(result)




