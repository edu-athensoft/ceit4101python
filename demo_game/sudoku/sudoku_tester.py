"""
test code
"""

from sudoku_init import *
from checker import *
from printer import *

data = getData()
datamap = DataMap(data)

ROWS = datamap.getRows()
COLS = datamap.getColumns()
BLOCKS = datamap.getBlocks()

print("== map ===")
printMap(data)
print()

"""
print("== rows ===")
printRow(ROWS, 0)
print()

print("== cols ===")
printColumn(COLS, 0)
print()

print("=== blocks ===")
printBlock(BLOCKS, 0)

print("=== test block by index ===")
print(f"Block #{0} = {datamap.getBlockByIndex(0)}")
print(f"Block #{0} = {datamap.getBlockSeqByIndex(0)}")
print()
print()

print("=== test row candidate ===")
isRowCandidate(ROWS[0], 5)
print()

print("=== test col candidate ===")
isColCandidate(COLS[0], 5)
print()

print("=== test block candidate ===")
isBlockCandidate(datamap.getBlockSeqByIndex(0), 5)
print()

print("=== test global candidate ===")
isCandidate(datamap, 5, 0, 0)
print()
"""

print("=== get possible candidates at index i,j ===")


def getCandidatesByIndex(i, j):
    cands = []
    for n in range(1, 10):
        if isCandidate(datamap, n, i, j):
            cands.append(n)
    return sorted(cands)


def scanForCandidates():
    candidatesList = []
    for i in range(9):
        for j in range(9):
            if datamap.data[i][j] == 0:
                cands = getCandidatesByIndex(i, j)
                print(f"({i},{j}) => {cands}")
                candidatesList.append((i, j, cands))
    return candidatesList


def getConfirmedNum_R1(candidatesList):
    """ return confirmed numbers by Rule No.1
        Rule 1.
        is a number is unique in its row, col,
        and block and it can be therefore determined.
    """
    confirmedNumbers = []

    for record in candidatesList:
        i, j, cands = record[0], record[1], record[2]
        if len(cands) == 1:
            confirmedNumbers.append((cands[0], i, j))

    return confirmedNumbers


def getConfirmedNum_R2(candidatesList):
    """ return confirmed numbers by Rule No.2
        Rule 2.
        is a number occurs only once at its row, or columns, or block
        and can be therefore determined.
    """
    cands_by_row = [[] for x in range(9)]

    def findNum(candidatesList, row_no, target):
        mylist = filter(lambda item: item[0]==row_no, candidatesList)
        for record in mylist:
            i, j, cands = record[0], record[1], record[2]
            if target in cands:
                return (target, i, j)
        return None

    def reduce(row_no):
        cands_set = set(cands_by_row[row_no])
        for n in cands_set:
            if cands_by_row[row_no].count(n)==1:
                return n
        else:
            return -1

    for record in candidatesList:
        i, j, temp_cands = record[0], record[1], record[2]

        for x in range(9):
            if i == x:
                cands_by_row[x].extend(temp_cands)

    confirmedNumberList = []
    for x in range(9):
        n = reduce(x)
        if n > 0:
            if findNum(candidatesList, x, n):
                confirmedNumberList.append(findNum(candidatesList, x, n))
                print(f"Number found at ROW:{x} under Rule 2: {findNum(candidatesList, x, n)}")

    return confirmedNumberList


def sloveByRule2():
    round = 1
    while True:
        print(f"\n=== round {round} ===")
        confirmedNumberList = getConfirmedNum_R2(scanForCandidates())
        for item in confirmedNumberList:
            datamap.update(item[0], item[1], item[2])
        printMap(datamap.data)

        if len(confirmedNumberList) == 0:
            break

        round += 1


def sloveByRule1():
    """attempt by rule 1"""
    print("\nAttempts for Rule 1")

    round = 1
    while True:
        print(f"\n=== round {round} === ")
        confirmedNumberList = getConfirmedNum_R1(scanForCandidates())
        if len(confirmedNumberList) == 0:
            if datamap.isFinished():
                print("\nDone.")
            else:
                print("\nNeed further work.")
                print("\nAttempts for other rules")
                # sloveByRule2()
            break
        else:
            print(confirmedNumberList)
            for item in confirmedNumberList:
                datamap.update(item[0], item[1], item[2])
            printMap(datamap.data)
            round += 1




# test

sloveByRule2()
sloveByRule1()

# sloveByRule2()
# sloveByRule1()




