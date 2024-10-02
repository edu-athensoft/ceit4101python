"""
quiz 332

4. Print out prime numbers in the range of 1 to 1000.
Prime numbers are positive, non-zero numbers that have exactly two factors - no more, no less.

get the total number of prime numbers
"""

import math

count = 0
for n in range(1, 1001):
    # prime numbers starts from 2
    if n > 1:
        for factor in range(2, int(math.sqrt(n))+1):
            if n % factor == 0:
                break
        else:
            print(f"Prime number: {n}")
            count += 1

print(f"Total {count} prime numbers")

