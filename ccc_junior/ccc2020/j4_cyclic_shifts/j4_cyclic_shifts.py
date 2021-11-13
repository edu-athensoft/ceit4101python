"""
CCC 2020 Junior
Problem J4. Cyclic Shifts

status:
AC

(without break statement)
Resources: 0.792s, 10.22 MB
Maximum runtime on single test case: 0.060s
Final score: 15/15 (5.0/5 points)

(with break statement)
Resources: 0.791s, 10.09 MB
Maximum runtime on single test case: 0.060s
Final score: 15/15 (5.0/5 points)
"""

# T = 'ABCCDEABAA'
# S = 'ABCDE'

T = input()
S = input()

# get all forms of S
def getAllCyclic(s):
    shifts = []
    for i in range(len(s)):
        shifts.append(s)
        s=s[1:]+s[0]
    return shifts

# print(getAllCyclic(S))

shifts = getAllCyclic(S)

result = 'no'
for shift in shifts:
    if shift in T:
        result = 'yes'
        break

print(result)

