"""
quiz 332

2. Please write a program to print out the following matrix and do not use nested for-loops.
Expected output:
1	2	3	4	5
6	7	8	9	10
11	12	13	14	15
Hint:  Using for-loop

"""

count = 0
N = 15
for i in range(1, N+1):  # Total 15 numbers (3x5)
    print(i, end='\t')  # Print 'a' with a tab space
    count += 1

    # After every 3 'a' characters, print a new line
    # removing the last blank line
    if count % 5 == 0 and count < N:
        print()