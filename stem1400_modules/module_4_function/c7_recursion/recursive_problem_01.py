#!/usr/bin/python3

"""
Input a string, then
reverse it and print out
one char by one and each char takes one line

key point:
each time, the function print out the last char at the index of (l-1)
and the length (l) decreases by one right after,
when l reaches 0, it comes to stop

"""


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string:')
l = len(s)
output(s, l)
