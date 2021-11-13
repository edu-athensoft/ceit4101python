"""
CCC 2019 Junior
Problem J1. Winning Score

formula:
score_a = a_3p * 3 + a_2p * 2 + a_1p

status:
Resources: 0.351s, 9.34 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""

# input
# Apples
a_3p = int(input())
a_2p = int(input())
a_1p = int(input())

# Bananas
b_3p = int(input())
b_2p = int(input())
b_1p = int(input())

# process
score_a = a_3p * 3 + a_2p * 2 + a_1p
score_b = b_3p * 3 + b_2p * 2 + b_1p

if score_a == score_b:
    print('T')
elif score_a > score_b:
    print('A')
else:
    print('B')


