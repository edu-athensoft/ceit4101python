"""
CCC 2021 Junior
J5/S2. Modern art

"""

# max row
# M = input()
M = 4

# max col
# N = input()
N = 5

# max lines
# K = input()
K = 7

line1 = 'R 3'
line2 = 'C 1'
line3 = 'C 2'
line4 = 'R 2'
line5 = 'R 2'
line6 = 'C 1'
line7 = 'R 4'

lines = []
lines.append(line1)
lines.append(line2)
lines.append(line3)
lines.append(line4)
lines.append(line5)
lines.append(line6)
lines.append(line7)

# set_lines = set(lines)
# lines = list(set_lines)
# lines.sort()
# print(lines)

# canvas =[['B']*N]*M
canvas =[[False]*N for i in range(M)]


# process
# def printCanvas(canvas):
#     for rows in canvas:
#         for col in rows:
#             print(col,end='')
#         print()

def paint(line):
    direction, index = line.split()
    # print(f'{direction}:{index}')
    index = int(index)

    if direction == 'R':
        for i in range(N):
            canvas[index-1][i] = not canvas[index-1][i]

    if direction == 'C':
        for i in range(M):
            canvas[i][index-1] = not canvas[i][index-1]

for line in lines:
    # print(line)
    paint(line)


# output canvas
count =0
for i in range(M):
    for j in range(N):
        if canvas[i][j]:
            count +=1
print(count)
# printCanvas(canvas)

