"""
1. Write a Python program to generate a 3*2 2D array whose each element is *.

list comprehension
"""

X = 3
Y = 2

arr_2d = []
arr_y = []

ELEMENT = '*'

for j in range(Y):
    arr_y.append(ELEMENT)

for i in range(X):
    arr_2d.append(arr_y)


print(arr_2d)