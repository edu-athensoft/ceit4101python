"""
generator

# t2 = []
# t2.append(t1[0])
# t2.append(t1[0]+t1[1])
# t2.append(t1[1]+t1[2])
# t2.append(t1[2])
#
# print(t2)
"""


# t0 = [1]
# t1 = [1, 1]
# t1 = [1, 2, 1]

def getNextLine(line):
    next = []
    length = len(line)
    next.append(line[0])
    for i in range(len(line)):
        if i < length - 1:
            next.append(line[i] + line[i + 1])
        else:
            next.append(line[i])
    return next


def f():
    line = [1]
    while True:
        next = getNextLine(line)
        yield next
        line = next
    return


# necessary
g = f()
triangle = []
triangle.append([1])
N = 10
for i in range(N):
    triangle.append(next(g))

print(triangle)
