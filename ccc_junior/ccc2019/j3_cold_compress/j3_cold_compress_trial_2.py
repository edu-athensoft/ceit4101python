"""
CCC 2019 Junior
Problem J3. cold compress

status:
AC

Resources: 0.127s, 9.30 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (5.0/5 points)

sample input:
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555
"""


# input
N = int(input())

for i in range(N):
    sample_str = input()

    last = sample_str[0]
    count = 0
    result = ''

    for index, char in enumerate(sample_str):
        if last == char:
            count += 1
        else:
            result += str(count)+" "+last+" "
            count = 1

        last = char

    result += str(count)+" "+last
    print(result)


