"""
CCC 2021 Junior
J5/S2. Modern art

Batch #1 (1/1 points)
Case #1:	AC	[0.026s,	9.45 MB]
Case #2:	AC	[0.026s,	9.45 MB]
Case #3:	AC	[0.026s,	9.45 MB]

Batch #2 (4/4 points)
Case #1:	AC	[0.026s,	9.45 MB]
Case #2:	AC	[0.028s,	9.45 MB]
Case #3:	AC	[0.026s,	9.45 MB]

Test case #3:	AC	[0.025s,	9.45 MB]	(0/0)
Test case #4:	AC	[0.025s,	9.45 MB]	(0/0)

Batch #5 (5/5 points)
Case #1:	AC	[0.028s,	9.45 MB]
Case #2:	AC	[0.028s,	9.45 MB]

Batch #6 (0/5 points)
Case #1:	TLE	[>3.000s,	113.27 MB]
Case #2:	—
Case #3:	—
Case #4:	—


Resources: ---, 113.27 MB
Final score: 10/15 (4.667/7 points)

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

canvas = [['B'] * N for i in range(M)]


def reverse(color):
    if color == 'B':
        color = 'G'
    else:
        color = 'B'
    return color


# process
# def printCanvas(canvas):
#     for rows in canvas:
#         for col in rows:
#             print(col, end='')
#         print()


def paint(line):
    direction, index = line.split()
    # print(f'{direction}:{index}')
    index = int(index)

    if direction == 'R':
        for i in range(N):
            canvas[index - 1][i] = reverse(canvas[index - 1][i])

    elif direction == 'C':
        for i in range(M):
            canvas[i][index - 1] = reverse(canvas[i][index - 1])

    else:
        pass


for line in lines:
    paint(line)

# output canvas
# printCanvas(canvas)

# output result
count = 0
for row in canvas:
    for col in row:
        if col == 'G':
            count += 1

print(count)
