"""
immutable elements
"""

t1 = ("mouse", [8, 4, 6], (1, 2, 3))
t2 = ("mouse", (8, 4, 6), (1, 2, 3))
t3 = ("mouse", {8, 4, 6}, (1, 2, 3))
t4 = ("mouse", {8: 88, 4: 44, 6: 66}, (1, 2, 3))

print(t1, type(t1))
print(t2, type(t1))
print(t3, type(t1))
print(t4, type(t1))
