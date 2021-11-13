"""
CCC 2020 Junior
Problem J1. Dog treats

formula:
1xS + 2xM + 3xL

status:
not submitted yet
"""

# input
s = int(input())
m = int(input())
l = int(input())

# process
score = s + 2*m + 3*l

# output
# pay attention to the case (in lower case)
if score >= 10:
    print('happy')
else:
    print('sad')

