"""
CCC 2020 Junior
Problem J2. Epidemiology

when

model:


status:  TLE
Batch #2 (0/15 points)
Case #1:	AC	[0.025s,	9.29 MB]
Case #2:	AC	[0.025s,	9.29 MB]
Case #3:	TLE	[>3.000s,	9.29 MB]

Resources: ---, 9.29 MB
Final score: 0/15 (0.0/3 points)
"""

# input
# P - total person number
P = int(input())
# initial infected people at day0
N = int(input())
# affected number per person
R = int(input())

# process
sum = N
i = 0

while True:
    i += 1
    sum += N *(R ** i)
    if sum > P:
        print(i)
        break


