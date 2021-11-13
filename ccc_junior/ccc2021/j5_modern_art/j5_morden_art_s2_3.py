"""
CCC 2021 Junior
J5/S2. Modern art

change to int from String
B = 1
G = -1

remove all paired lines

result = numOfRowOfLine * N + numOfColOfLine * M - 2 * numOfRowOfLine * numOfColOfLine

why double numOfRowOfLine * numOfColOfLine ?
because:
1. the number of cross should be counted once.
2. in addition, the crossed point flipped for twice and back to its original state


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

numOfRowOfLine = 0
numOfColOfLine = 0

for line in lines:
    if line[0] =='R':
        numOfRowOfLine += 1
    if line[0] =='C':
        numOfColOfLine += 1

result = numOfRowOfLine * N + numOfColOfLine * M - 2 * numOfRowOfLine * numOfColOfLine
print(result)


"""

"""