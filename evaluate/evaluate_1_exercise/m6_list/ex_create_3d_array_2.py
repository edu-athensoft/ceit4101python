"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.

list comprehension
"""

X = 3
Y = 2
Z = 3

arr_3d = []
arr_y = []
arr_z = []

ELEMENT = '*'

for k in range(Z):
    arr_z.append(ELEMENT)

for j in range(Y):
    arr_y.append(arr_z)

for i in range(X):
    arr_3d.append(arr_y)

print(arr_3d)