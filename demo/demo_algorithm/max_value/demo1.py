"""
if a,b,c,d are positive integers with a sum of 63
What's the maximum value of ab+bc+cd?
"""

# a_min = 1
# b_min = 1
# c_min = 1
# d_min = 1

SUM = 63
A_MAX = B_MAX = C_MAX = D_MAX = SUM-3

# res = []
res = {}
for a in range(1, A_MAX+1):
    for b in range(1, B_MAX+1-a):
        for c in range(1, C_MAX+1-a-b):
            d = SUM-a-b-c
            value = a*b+b*c+c*d
            # res.append(a*b+b*c+c*d)
            res[value]=(a,b,c,d)

print(len(res), max(res), res[max(res)])
