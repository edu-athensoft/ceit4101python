#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Fibonacci sequence
0,1,1,2,3,5,8,13,21,...

Input n and get the n-th number in the sequence

key point:
f(n)=f(n-2)+f(n-1)   when n>2
f(1) = 0
f(2) = 1
"""


# recursion
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


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
