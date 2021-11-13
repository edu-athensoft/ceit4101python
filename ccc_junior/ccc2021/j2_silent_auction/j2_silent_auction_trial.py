"""
Problem J2. Silent Auction

Resources: 0.225s, 9.31 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""
WINNER_NAME = None
WINNER_BID = -1

N = int(input())

for i in range(N):
    name = input()
    bid = int(input())

    if bid > WINNER_BID:
        WINNER_NAME = name
        WINNER_BID = bid

print(WINNER_NAME)

