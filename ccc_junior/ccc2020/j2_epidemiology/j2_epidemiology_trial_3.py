"""
CCC 2020 Junior
Problem J2. Epidemiology

status:
AC

Resources: 2.278s, 9.40 MB
Maximum runtime on single test case: 1.877s
Final score: 15/15 (3.0/3 points)

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
lastDayNum = sum

while True:
    i += 1
    # lastDayNum = lastDayNum * R
    lastDayNum *= R
    sum += lastDayNum
    if sum > P:
        print(i)
        break


