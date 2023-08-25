"""
Sudoku Cracker
version: 1.0
"""

from sudoku_init import *
from printer import *


# Init
data = getData()
datamap = DataMap(data)

ROWS = datamap.getRows()
COLS = datamap.getColumns()
BLOCKS = datamap.getBlocks()

# main

