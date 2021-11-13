"""
Problem J1. Boiling Water

Resources: 0.177s, 9.30 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

B = int(input())

P = 5*B - 400

seaLevel = None
if B > 100:
    seaLevel = -1
elif B == 100:
    seaLevel = 0
else:
    seaLevel = 1

print(P)
print(seaLevel)
