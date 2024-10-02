"""
quiz 332 - q1

1. Please write a program to print out a matrix of char 'a' and do not use nested for-loops.
Expected output:
a	a	a
a	a	a
a	a	a
Hint:  Using for-loop

"""


count = 0
for _ in range(9):  # Total 9 'a' characters (3x3)
    print('a', end='\t')  # Print 'a' with a tab space
    count += 1
    if count % 3 == 0:  # After every 3 'a' characters, print a new line
        print()

