"""
checker
"""


def isRowCandidate(row, target):
    # print(f"DATA: ROW={row}")
    flag = False
    if target not in row:
        flag = True
        # print(f"INFO: {target} is a ROW candidate.")
    else:
        # print(f"INFO: {target} is not a ROW candidate.")
        pass
    return flag


def isColCandidate(col, target):
    # print(f"DATA: COL={col}")
    flag = False
    if target not in col:
        flag = True
        # print(f"INFO: {target} is a COL candidate. ")
    else:
        # print(f"INFO: {target} is not a COL candidate.")
        pass
    return flag


def isBlockCandidate(blockseq, target):
    # print(f"DATA: BLOCK={blockseq}")
    flag = False
    if target not in blockseq:
        flag = True
        # print(f"INFO: {target} is a BLOCK candidate. ")
    else:
        # print(f"INFO: {target} is not a BLOCK candidate.")
        pass
    return flag


def isCandidate(datamap, target, i, j):
    flag = False
    isFitRow = isRowCandidate(datamap.getRows()[i], target);
    isFitCol = isColCandidate(datamap.getColumns()[j], target)
    block_no = datamap.getBlockIndex(i, j)
    isFitBlock = isBlockCandidate(datamap.getBlockSeqByIndex(block_no), target)
    flag = isFitRow and isFitCol and isFitBlock
    # print(f"{target} at ({i},{j}) is a candidate? {flag}")
    return flag