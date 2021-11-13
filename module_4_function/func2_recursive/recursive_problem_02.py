#!/usr/bin/python3

"""
Input a string, then
print it out
one char by one and each char takes one line

key point:
each time, the function print out the char at the index of i
and i increases by one right after,
when it reaches the length of the string, it comes to stop
"""


def output(s, i):
    if i == len(s):
        return
    print(s[i])
    output(s, i+1)


s = input('Input a string:')
l = 0
output(s, l)
