"""
Write a python program to test how fast your program runs.
Hints:
Write a loop and make it repeat for at least 1,000,000 times.
"""

from datetime import datetime


def testspeed(N=1000000):
    before = datetime.now()
    dotask(N)
    after = datetime.now()

    time_escaped = after - before
    print(f"Time escaped for N={N}: {time_escaped}")


def dotask(N):
    mystr = ""
    for _ in range(N):
        mystr += str(_)


# main
testspeed(500000)
testspeed()
testspeed(2000000)
