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

lines = []
for i in range(K):
    lines.append(input())

canvas =[[False for j in range(N)] for i in range(M)]

def paint(line):
    direction, index = line.split()
    index = int(index)

    if direction == 'R':
        for i in range(N):
            canvas[index-1][i] = not canvas[index-1][i]
    if direction == 'C':
        for i in range(M):
            canvas[i][index-1] = not canvas[i][index-1]

for line in lines:
    paint(line)

# output canvas
count =0
for i in range(M):
    for j in range(N):
        if canvas[i][j]:
            count +=1
print(count)

