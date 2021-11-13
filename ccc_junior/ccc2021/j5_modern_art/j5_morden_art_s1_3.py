"""
CCC 2021 Junior
J5/S2. Modern art

change to int from String
B = 1
G = -1

removed paired Rows and Cols

Batch #1 (1/1 points)
Case #1:	AC	[0.025s,	9.44 MB]
Case #2:	AC	[0.026s,	9.44 MB]
Case #3:	AC	[0.025s,	9.44 MB]

Batch #2 (4/4 points)
Case #1:	AC	[0.026s,	9.44 MB]
Case #2:	AC	[0.025s,	9.44 MB]
Case #3:	AC	[0.025s,	9.44 MB]

Test case #3:	AC	[0.025s,	9.44 MB]	(0/0)
Test case #4:	AC	[0.025s,	9.44 MB]	(0/0)

Batch #5 (5/5 points)
Case #1:	AC	[0.027s,	9.44 MB]
Case #2:	AC	[0.027s,	9.44 MB]

Batch #6 (0/5 points)
Case #1:	TLE	[>3.000s,	10.47 MB]
Case #2:	—
Case #3:	—
Case #4:	—


Resources: ---, 10.47 MB
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
    raw = input()
    if raw not in lines:
        lines.append(raw)
    else:
        lines.remove(raw)

canvas = [[1] * N for i in range(M)]


def paint(line):
    direction, index = line.split()
    index = int(index)

    if direction == 'R':
        for i in range(N):
            canvas[index - 1][i] = (-1)*(canvas[index - 1][i])
    elif direction == 'C':
        for i in range(M):
            canvas[i][index - 1] = (-1)*(canvas[i][index - 1])
    else:
        pass


for line in lines:
    paint(line)

# output result
count = 0
for row in canvas:
    for col in row:
        if col == -1:
            count += 1
print(count)
