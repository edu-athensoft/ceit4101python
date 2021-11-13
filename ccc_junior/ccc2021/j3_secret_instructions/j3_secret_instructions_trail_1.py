"""
Problem J3. Secret instructions
"""

def process(strNum):
    # print(f'do process on {strNum}')
    if strNum == '99999':
        return

    direction = None
    global CURRENT_DIR

    if strNum[0:2]== '00':
        direction = CURRENT_DIR
    else:
        # left or right
        dirNum = int(strNum[0])+int(strNum[1])
        if dirNum%2 == 1 :
            direction = 'left'
        else:
            direction = 'right'
        CURRENT_DIR = direction

    print(f'{direction} {strNum[2:]}')



list_numbers = []

while(True):
    str_num = input("input 5 digit number:")
    list_numbers.append(str_num)
    if str_num == '99999':
        break

# test
# print(list_numbers)

# global
CURRENT_DIR = None

# process
for str_num in list_numbers:
    process(str_num)
