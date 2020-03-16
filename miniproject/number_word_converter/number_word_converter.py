"""
number word converter
"""

dict_number = {
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
    "0": "ZERO",
}

numbers = input("enter your number in integer:")

for digit in numbers:
    print(dict_number[digit], end=" ")

