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
    if line.split()[0].strip() =='R':
        numOfRowOfLine += 1
    if line.split()[0].strip() =='C':
        numOfColOfLine += 1

result = numOfRowOfLine * N + numOfColOfLine * M - 2 * numOfRowOfLine * numOfColOfLine
print(result)


"""
Batch #1 (1/1 points)
Case #1:	AC	[0.025s,	9.32 MB]
Case #2:	AC	[0.025s,	9.32 MB]
Case #3:	AC	[0.025s,	9.32 MB]

Batch #2 (4/4 points)
Case #1:	AC	[0.025s,	9.32 MB]
Case #2:	AC	[0.025s,	9.32 MB]
Case #3:	AC	[0.025s,	9.32 MB]

Test case #3:	AC	[0.025s,	9.32 MB]	(0/0)
Test case #4:	AC	[0.025s,	9.32 MB]	(0/0)

Batch #5 (5/5 points)
Case #1:	AC	[0.025s,	9.32 MB]
Case #2:	AC	[0.025s,	9.32 MB]

Batch #6 (0/5 points)
Case #1:	TLE	[>3.000s,	10.48 MB]
Case #2:	—		
Case #3:	—		
Case #4:	—		


Resources: ---, 10.48 MB
Final score: 10/15 (4.667/7 points)
"""