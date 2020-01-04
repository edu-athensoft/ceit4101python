# get the summary of a number list

"""
round 0:    numbers[0]+ sum -> sum
round 1:    numbers[1]+ sum -> sum
...
round i:    numbers[i]+ sum -> sum
...
round 9:    numbers[9]+ sum -> sum

get sum
"""

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum = 0

for item in numbers:
    sum += item

print("sum=",sum)




