"""
print data
data_map, rows, columns, blocks
"""


def printMap(data):
    for i in range(9):
        for j in range(9):
            if data[i][j]:
                print(data[i][j], end="\t")
            else:
                print(0, end="\t")
            if j % 3 == 2:
                print(' ', end='\t')
        print()
        if i % 3 == 2:
            print()


def printRow(ROWS, row_no):
    print(ROWS[row_no])


def printColumn(COLS, col_no):
    print(COLS[col_no])


def printBlock(BLOCKS, block_no):
    # print(BLOCKS[block_no])
    for i in range(3):
        for j in range(3):
            print(BLOCKS[block_no][i][j], end="\t")
        print()
    print()
