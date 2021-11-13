"""
CCC 2020 Junior
Problem J2. Epidemiology

when

model:


status:  TLE

"""

# input
# P - total person number
P = int(input())
# initial infected people at day0
N = int(input())
# affected number per person
R = int(input())

# process
sum = 1
i = 0
pn = P/N

while True:
    i += 1
    sum += R ** i
    if sum > pn:
        print(i)
        break

