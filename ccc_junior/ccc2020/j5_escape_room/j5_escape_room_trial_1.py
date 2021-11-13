"""
CCC 2020 Junior
Problem J5. Escape room


Batch #1 (0/0 points)
Case #1:	AC	[0.026s,	9.35 MB]

Batch #2 (0/1 points)
Case #1:	AC	[0.025s,	9.35 MB]
Case #2:	AC	[0.025s,	9.35 MB]
Case #3:	AC	[0.025s,	9.35 MB]
Case #4:	AC	[0.025s,	9.35 MB]
Case #5:	AC	[0.025s,	9.35 MB]
Case #6:	IR (RecursionError)	[0.030s,	10.46 MB]
Case #7:	—

"""

M = 3
N = 4
map=[[3, 10, 8, 14],
     [1, 11, 12, 12],
     [6, 2, 3, 9]]


"""
# input
# row
M = int(input())
# column
N = int(input())
# cells
map = []
for m in range(M):
    line = input().split()
    for i, v in enumerate(line):
        line[i] = int(v)
    map.append(line)
"""

def hasPrevExitCellValue(exitR, exitC):
    global result
    lastCells = []
    for i in range(exitR):
        for j in range(exitC):
            # print(map[i][j])
            if map[i][j] == exitR*exitC:
                lastCells.append((i+1, j+1, map[i][j]))

    # print(lastCells)
    for cell in lastCells:
        print(cell)
        # the entrance is found
        if cell[0] == 1 and cell[1] == 1:
            result = 'yes'
            return
        else:
            # print('not yet')
            # print(cell[0],cell[1],cell[2])
            hasPrevExitCellValue(cell[0], cell[1])

    # return lastCells

result = 'no'
hasPrevExitCellValue(M, N)
print(result)


"""
Batch #1 (0/0 points)
Case #1:	AC	[0.026s,	9.35 MB]

Batch #2 (0/1 points)
Case #1:	AC	[0.025s,	9.35 MB]
Case #2:	AC	[0.025s,	9.35 MB]
Case #3:	AC	[0.025s,	9.35 MB]
Case #4:	AC	[0.025s,	9.35 MB]
Case #5:	AC	[0.025s,	9.35 MB]
Case #6:	IR (RecursionError)	[0.030s,	10.46 MB]
Case #7:	—		

Batch #3 (0/2 points)
Case #1:	AC	[0.025s,	9.35 MB]
Case #2:	WA	[0.025s,	9.35 MB]
Case #3:	—		
Case #4:	—		
Case #5:	—		
Case #6:	—		

Batch #4 (0/4 points)
Case #1:	AC	[0.025s,	9.35 MB]
Case #2:	AC	[0.025s,	9.35 MB]
Case #3:	WA	[0.025s,	9.35 MB]
Case #4:	—		
Case #5:	—		

Batch #5 (0/4 points)
Case #1:	AC	[0.025s,	9.35 MB]
Case #2:	AC	[0.026s,	9.41 MB]
Case #3:	WA	[0.025s,	9.35 MB]
Case #4:	—		

Batch #6 (0/2 points)
Case #1:	AC	[0.041s,	10.79 MB]
Case #2:	AC	[0.041s,	10.17 MB]
Case #3:	WA	[0.042s,	10.79 MB]
Case #4:	—		
Case #5:	—		
Case #6:	—		

Batch #7 (0/2 points)
Case #1:	AC	[0.412s,	48.91 MB]
Case #2:	WA	[0.429s,	37.24 MB]
Case #3:	—		
Case #4:	—		
Case #5:	—		
Case #6:	—		
Case #7:	—		


Resources: 1.352s, 48.91 MB
Final score: 0/15 (0.0/10 points)
"""








