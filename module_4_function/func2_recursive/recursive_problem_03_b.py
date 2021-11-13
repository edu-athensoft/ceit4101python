#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Fibonacci sequence
0,1,1,2,3,5,8,13,21,...

Input n and get the n-th number in the sequence

key point:
a = 0,      b = 1
a = 1 = b,  b = 1 = last_a + b
a = 1 = b,  b = 2 = last_a + b

"""


# iteration
def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        # a, b = b, a + b
        last_a = a
        a = b
        b = last_a+b
    return a


# test n
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
print(fib(10))