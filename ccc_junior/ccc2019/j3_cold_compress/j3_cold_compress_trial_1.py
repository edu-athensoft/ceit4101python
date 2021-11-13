"""
CCC 2019 Junior
Problem J3. cold compress

status:

sample input:
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555
"""


sample_str = '+++===!!!!'
sample_str = '777777......TTTTTTTTTTTT'
sample_str = '3.1415555'

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


