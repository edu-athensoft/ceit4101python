"""
BOM Table and Calculator
"""

CARD_TARGET = 'TARGET CARD'
CARD_ANY = 'OTHER CARD'
CARD = None


S4 = (CARD_ANY,)
S4_1 = S4 * 3
S5 = S4_1 * 3
S5_1 = S5 * 2
S6 = S5_1 * 3
S6_1 = S6 * 2
S7 = S6_1 * 3
S7_1 = S7 * 3
S7_2 = S7_1 * 3

T4 = (CARD_TARGET,)
T4_1 = T4 * 3
T5 = T4_1 * 1
T5_1 = T5 * 2
T6 = T5_1 * 1
T6_1 = T6 * 2
T7 = T6_1 * 1
T7_1 = T7 * 3
T7_2 = T7_1 * 1

C4 =    T4
C4_1 =  C4 * 3
C5 =    T4_1 + S4_1 * 2
C5_1 =  C5 * 2
C6 =    C5_1 + S5_1 * 2
C6_1 =  C6 * 2
C7 =    C6_1 + S6_1 * 2
C7_1 =  C7 * 3
C7_2 =  C7_1 + S7_1 * 2

card_dict_any = {
    'S4': S4,
    'S4_1': S4_1,
    'S5': S5,
    'S5_1': S5_1,
    'S6': S6,
    'S6_1': S6_1,
    'S7': S7,
    'S7_1': S7_1,
    'S7_2': S7_2
}

card_dict_target = {
    'T4': T4,
    'T4_1': T4_1,
    'T5': T5,
    'T5_1': T5_1,
    'T6': T6,
    'T6_1': T6_1,
    'T7': T7,
    'T7_1': T7_1,
    'T7_2': T7_2
}

card_dict = {
    'C4':   C4,
    'C4_1': C4_1,
    'C5':   C5,
    'C5_1': C5_1,
    'C6':   C6,
    'C6_1': C6_1,
    'C7':   C7,
    'C7_1': C7_1,
    'C7_2': C7_2
}


def getnum_any(card_item):
    card_num = card_item[1].count(CARD_ANY)
    return card_item[0], card_num


def getnum_target(card_item):
    card_num = card_item[1].count(CARD_TARGET)
    return card_item[0], card_num


def getlevel_next(card_star_name):
    """
    get the number of next star level card based on current star level card
    :param card_star:
    :return:
    """
    if card_star_name in CARD_STAR_LIST:
        next_level_card_star_name = CARD_STAR_LIST[CARD_STAR_LIST.index(card_star_name)+1]
        print(f"current level: {card_star_name}, next level: {next_level_card_star_name}")
    else:
        print(f"input level: {card_star_name}, No such card star level")
    return next_level_card_star_name


def getlevel_prev(card_star_name):
    """
    get the number of next star level card based on current star level card
    :param card_star:
    :return:
    """
    if card_star_name in CARD_STAR_LIST:
        next_level_card_star_name = CARD_STAR_LIST[CARD_STAR_LIST.index(card_star_name)-1]
        print(f"current level: {card_star_name}, previous level: {next_level_card_star_name}")
    else:
        print(f"input level: {card_star_name}, No such card star level")
    return next_level_card_star_name


def getcomponent(card_star_name):
    # print('card_star_name=',card_star_name)
    # return card_dict_any[card_star_name]
    card_star_name = card_star_name.replace('S','C')
    return card_dict[card_star_name]


def get_result(myinput):
    # myinput = 's4'
    myinput = myinput.strip().replace('.','_').upper()

    print(f"{myinput} needs:",end='\t')
    result = getcomponent(myinput)
    print(f'{CARD_TARGET} x {result.count(CARD_TARGET)} and {CARD_ANY} x {result.count(CARD_ANY)}')
    # print(result)
    print("")

# main program
print("==============================")
print("==={:^24s}===".format('Warpath Calculator'))
print("==={:^24s}===".format('Ver 1.0'))
print("==={:^24s}===".format('written by MoraxLapis'))
print("==={:^24s}===".format('Alliance: [WIAW] @ Server 16'))
print("==============================")

print("\nHints:")
print("""This program tells you how many 
target cards you should collect.""")


print()
print("Card name list")
CARD_STAR_LIST = list(card_dict_any.keys())
str_card_list = str(CARD_STAR_LIST)
# print(CARD_STAR_LIST)
MAX_WIDTH = 34
char_pos = 0
for char in str_card_list:
    print(char,end='')
    char_pos += 1
    if char_pos == MAX_WIDTH:
        char_pos = 0
        print()
print("\n")

print("------------------------------")
print("If you starts from a **** card")
print("------------------------------")
for card in CARD_STAR_LIST:
    get_result(card)

"""
next_cardname = getlevel_next(myinput)
print(getcomponent(next_cardname))
print()

prev_cardname = getlevel_prev(myinput)
print(getcomponent(prev_cardname))
"""

# print("The number list of total card you need for each star level:")
# for card_item in card_dict_any.items():
#     card_name, cnum = getnum_any(card_item)
#     print(f'{card_name}: x {cnum}')
#
# print()
#
# print("The number list of your target card for each star level:")
# for card_item in card_dict_target.items():
#     card_name, cnum = getnum_target(card_item)
#     print(f'{card_name}: x {cnum}')