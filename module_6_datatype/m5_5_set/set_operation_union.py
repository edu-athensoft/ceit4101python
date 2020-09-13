# set operation
# union

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

d = ['b','c']

# C = A + B

C = A | B
print(C)

C = A.union(B)
print(C)

C = B.union(A)
print(C)

C = B.union(d)
print(C)