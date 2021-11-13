"""
CCC 2021 Junior
J5/S2. Modern art

"""

# max row
M = int(input())
# max col
N = int(input())
# max lines
K = int(input())

ROWS = [False]*M
COLS = [False]*N

for i in range(K):
    rowOrCol, index = input().split()
    index = int(index) -1
    if rowOrCol =='R':
        ROWS[index] = not ROWS[index]
    if rowOrCol =='C':
        COLS[index] = not COLS[index]

numOfRowOfLine = ROWS.count(True)
numOfColOfLine = COLS.count(True)

print(numOfRowOfLine * N + numOfColOfLine * M - 2 * numOfRowOfLine * numOfColOfLine)


"""
Batch #1 (1/1 points)
Case #1:	AC	[0.025s,	9.40 MB]
Case #2:	AC	[0.025s,	9.40 MB]
Case #3:	AC	[0.025s,	9.40 MB]

Batch #2 (4/4 points)
Case #1:	AC	[0.025s,	9.40 MB]
Case #2:	AC	[0.025s,	9.40 MB]
Case #3:	AC	[0.025s,	9.40 MB]

Test case #3:	AC	[0.025s,	9.40 MB]	(0/0)
Test case #4:	AC	[0.025s,	9.40 MB]	(0/0)

Batch #5 (5/5 points)
Case #1:	AC	[0.025s,	9.40 MB]
Case #2:	AC	[0.025s,	9.40 MB]

Batch #6 (5/5 points)
Case #1:	AC	[1.105s,	20.69 MB]
Case #2:	AC	[1.128s,	20.69 MB]
Case #3:	AC	[1.025s,	9.41 MB]
Case #4:	AC	[1.060s,	9.41 MB]


Resources: 4.570s, 20.69 MB
Maximum runtime on single test case: 1.128s
Final score: 15/15 (7.0/7 points)
"""

