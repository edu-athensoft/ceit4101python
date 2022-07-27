"""
1. Write a Python program to display a number with a comma separator.

Basic idea:
cutting the string of number into groups by 3-digits

if the first group has less than 3 digits (like 1 or 2),
then filling it with leading zero

Join all substring with comma

Remove the leading zero and return


"""
import math

# mynum = 1234
# mystr = str(mynum)


def getFormattedNum(strNum):
    # length
    length = len(strNum)
    # print(length)

    # get number of group by 3 digits
    groupNum = math.ceil(length / 3)
    # print(groupNum)

    # fill with leading zero if necessary
    filledStrNum = strNum.zfill(groupNum * 3)
    # print(filledStrNum)

    # cut by group
    groupedNumStr = []
    for i in range(0, len(filledStrNum), 3):
        groupedNumStr.append(filledStrNum[i:i + 3])

    # join together
    result = ','.join(groupedNumStr)

    # remove leading zero
    processedNumStr = result.lstrip('0')

    return processedNumStr


# main
while True:
    mystr = input('Input a number: ')
    if mystr.isdigit():
        break

result = getFormattedNum(mystr)
print(result)
