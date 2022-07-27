"""
Game
Guessing a number - version 1

from 1 to 100
guessing a number you specified at the beginning for 5 times
each you guess, and you will get a response from the computer with "too small, too large, bingo"

if you got "bingo", then print out "Congras!"

if you failed for 5 times, then print out "Please try it again, dood"

Hints:
1.1 Difficulties
It is allowed to adjust the difficulty level by changing the number of times
"""

# case 1:  for loop
for a in range(5):
    print(a)

# print("===")

# case 2: while loop
counter = 5
i = 0
while i<5:
    print(i)
    i += 1


# hints:
# input() -> integer
# int(input("xxxx"))
# algorithm
# compare the target number with your current input
# if-else statement
# 5 times -> loop



