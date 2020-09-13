# set operation
# symmetric difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# A ^ B
C = A ^ B
print(C)

# C = A.difference(B)
# print(C)

# use symmetric_difference function on A
d = A.symmetric_difference(B)
print(d)

# use symmetric_difference function on B
d = B.symmetric_difference(A)
print(d)

