"""
Problem J3. Secret instructions

Resources: 0.303s, 9.41 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (5.0/5 points)
"""


def process(strNum):
    if strNum == '99999':
        return

    # direction = None
    global CURRENT_DIR

    if strNum[0:2] == '00':
        direction = CURRENT_DIR
    else:
        # left or right
        dirNum = int(strNum[0]) + int(strNum[1])
        if dirNum % 2 == 1:
            direction = 'left'
        else:
            direction = 'right'
        CURRENT_DIR = direction

    print(f'{direction} {strNum[2:]}')


list_numbers = []
# global
CURRENT_DIR = None

while True:
    str_num = input()  # input 5 digit numbers
    list_numbers.append(str_num)
    if str_num == '99999':
        break

# process
for str_num in list_numbers:
    process(str_num)
