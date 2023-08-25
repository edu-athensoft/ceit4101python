"""
init
sudoku 1
input0 = [0, 9, 4, 0, 3, 0, 1, 0, 0]
input1 = [8, 1, 2, 7, 0, 0, 0, 9, 6]
input2 = [3, 0, 0, 1, 9, 0, 0, 0, 0]
input3 = [0, 3, 0, 9, 0, 4, 6, 0, 0]
input4 = [0, 0, 8, 6, 1, 3, 0, 4, 9]
input5 = [0, 0, 6, 2, 0, 0, 0, 0, 1]
input6 = [4, 0, 3, 5, 0, 0, 0, 0, 8]
input7 = [5, 0, 0, 0, 2, 0, 7, 0, 0]
input8 = [0, 6, 0, 0, 0, 8, 4, 1, 5]

sudoku 2
input0 = [0, 0, 0, 5, 0, 0, 3, 0, 0]
input1 = [0, 7, 0, 0, 3, 2, 0, 0, 5]
input2 = [0, 3, 0, 7, 6, 0, 0, 0, 9]

input3 = [0, 0, 0, 4, 0, 7, 0, 0, 8]
input4 = [0, 0, 0, 0, 0, 0, 0, 3, 0]
input5 = [2, 5, 0, 0, 0, 0, 9, 0, 7]

input6 = [7, 2, 0, 3, 0, 9, 5, 0, 0]
input7 = [8, 9, 0, 2, 0, 0, 0, 0, 0]
input8 = [0, 0, 5, 0, 0, 0, 0, 0, 6]

"""


def getData():
    input0 = [0, 0, 0, 5, 0, 0, 3, 0, 0]
    input1 = [0, 7, 0, 0, 3, 2, 0, 0, 5]
    input2 = [0, 3, 0, 7, 6, 0, 0, 0, 9]

    input3 = [0, 0, 0, 4, 0, 7, 0, 0, 8]
    input4 = [0, 0, 0, 0, 0, 0, 0, 3, 0]
    input5 = [2, 5, 0, 0, 0, 0, 9, 0, 7]

    input6 = [7, 2, 0, 3, 0, 9, 5, 0, 0]
    input7 = [8, 9, 0, 2, 0, 0, 0, 0, 0]
    input8 = [0, 0, 5, 0, 0, 0, 0, 0, 6]

    data = [input0, input1, input2,
            input3, input4, input5,
            input6, input7, input8]

    return data


class DataMap:
    def __init__(self, data):
        self.data = data
        self.rows = self.getRows()
        self.cols = self.getColumns()
        self.blocks = self.getBlocks()

    def update(self, target, i, j):
        """update value at (i,j) with target"""
        self.data[i][j] = target

    def getRows(self):
        rows = []
        for i in range(9):
            rows.append(self.data[i])
        return rows

    def getColumns(self):
        cols = []
        for j in range(9):
            col = []
            for i in range(9):
                col.append(self.data[i][j])
            cols.append(col)
        return cols


    def getBlocks(self):
        blocks = []

        def getBlock(startRow, startCol):
            endRow = startRow + 3
            endCol = startCol + 3
            block = []
            for i in range(startRow, endRow):
                row = []
                for j in range(startCol, endCol):
                    row.append(self.data[i][j])
                block.append(row)
            return block

        blocks.append(getBlock(0, 0))
        blocks.append(getBlock(0, 3))
        blocks.append(getBlock(0, 6))

        blocks.append(getBlock(3, 0))
        blocks.append(getBlock(3, 3))
        blocks.append(getBlock(3, 6))

        blocks.append(getBlock(6, 0))
        blocks.append(getBlock(6, 3))
        blocks.append(getBlock(6, 6))
        return blocks


    def getBlockByIndex(self, index):
        return self.blocks[index]

    def getBlockSeqByIndex(self, index):
        b = self.getBlockByIndex(index)
        seq =[]
        for i in range(3):
            for j in range(3):
                seq.append(b[i][j])

        # remove 0
        blockset = set(seq)
        blockset.remove(0)
        return sorted(list(blockset))

    def getBlockIndex(self, i, j):
        block_no = -1
        if 0<=i<=2:
            if 0<=j<=2:
                block_no = 0
            elif 3<=j<=5:
                block_no = 1
            else:
                block_no = 2
        elif 3<=i<=5:
            if 0<=j<=2:
                block_no = 3
            elif 3<=j<=5:
                block_no = 4
            else:
                block_no = 5
        else:
            if 0<=j<=2:
                block_no = 6
            elif 3<=j<=5:
                block_no = 7
            else:
                block_no = 8

        return block_no

    def isFinished(self):
        flag = True
        for i in range(9):
            for j in range(9):
                if self.data[i][j] == 0:
                   flag = False
        return flag