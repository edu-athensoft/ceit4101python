"""
CCC 2019 Junior
Problem J3. Time to decompress

status:
AC

Test case #1:	AC	[0.026s,	9.29 MB]	(3/3)
Test case #2:	AC	[0.025s,	9.29 MB]	(3/3)
Test case #3:	AC	[0.025s,	9.29 MB]	(3/3)
Test case #4:	AC	[0.025s,	9.29 MB]	(3/3)
Test case #5:	AC	[0.025s,	9.29 MB]	(3/3)


Resources: 0.126s, 9.29 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

# input
# line numbers
L = int(input())

output = []
# format:  N x
for i in range(L):
    N, x = input().split()
    N = int(N)
    output.append(x*N)

# output
# L lines
for line in output:
    print(line)




