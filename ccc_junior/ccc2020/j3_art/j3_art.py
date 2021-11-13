"""
CCC 2020 Junior
Problem J3. Art

status:
AC

Resources: 0.402s, 9.24 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""

# settings
xmax = 0
ymax = 0

xmin = 100
ymin = 100

# input
N = int(input())
for i in range(N):
    x, y = input().split(",")
    # test
    # print(f"x={x}, y={y}")
    x = int(x)
    y = int(y)

    if x < xmin:
        xmin = x
    if x > xmax:
        xmax = x
    if y < ymin:
        ymin = y
    if y > ymax:
        ymax = y

# output
xleft = xmin -1
yleft = ymin -1

xright = xmax + 1
yright = ymax + 1

print(f'{xleft},{yleft}')
print(f'{xright},{yright}')





