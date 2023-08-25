"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.

list comprehension
"""

X = 3
Y = 2
Z = 3

arry3d = [[ ['*' for m in range(X)] for n in range(Y)] for k in range(Z)]
print(arry3d)