"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument a with argument b and print the result.

Sample Input:
5
10
3

Sample Output:
20
30
"""

res1 = lambda a : a + 15
arg1 = int(input())

arg2 = int(input())
arg3 = int(input())
res2 = lambda a, b : a * b

print(res1(arg1))
print(res2(arg2, arg3))