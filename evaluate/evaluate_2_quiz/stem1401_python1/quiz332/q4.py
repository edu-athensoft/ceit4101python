"""
quiz 332

4. Print out prime numbers in the range of 1 to 1000.
Prime numbers are positive, non-zero numbers that have exactly two factors - no more, no less.
"""

for n in range(1, 1001):
    # prime numbers starts from 2
    if n > 1:
        for factor in range(2, n):
            if n % factor == 0:
                break
        else:
            print(f"Prime number: {n}")
