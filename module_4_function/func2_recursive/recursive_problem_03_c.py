#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Fibonacci sequence
0,1,1,2,3,5,8,13,21,...

Input n and get the sequence up to the n-th number

key point:
f(n)=f(n-2)+f(n-1)   when n>2
f(1) = 0
f(2) = 1
"""


# iteration
def fib(n):
    a, b = 0, 1
    fib_numbers = []
    for i in range(n):
        # a, b = b, a + b
        last_a = a
        a = b
        b = last_a+b
        fib_numbers.append(last_a)
    return fib_numbers


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