"""
Gacha-like Treasure Chest
version:    1.0
author:     Athens
date:       2021-02-22
org:        Athensoft Inc.
"""

import random


# prepare a chest with 1000 possible items
def create_chest():
    chest = []
    # for i in range(638):
    #     chest.append(ITEM1)
    # for i in range(250):
    #     chest.append(ITEM2)
    # for i in range(100):
    #     chest.append(ITEM3)
    # for i in range(10):
    #     chest.append(ITEM4)
    # for i in range(2):
    #     chest.append(ITEM5)

    list1 = [ITEM1] * 638
    list2 = [ITEM2] * 250
    list3 = [ITEM3] * 100
    list4 = [ITEM4] * 10
    list5 = [ITEM5] * 2
    chest = list1 + list2+list3+ list4+list5
    random.shuffle(chest)
    return chest


# trials
def open_chests(t):
    def get_item(mychest):
        return random.choice(mychest)

    for i in range(t):
        item = get_item(mychest)
        if item==ITEM1:
            rank1_items.append(item)
        elif item==ITEM2:
            rank2_items.append(item)
        elif item==ITEM3:
            rank3_items.append(item)
        elif item==ITEM4:
            rank4_items.append(item)
        elif item==ITEM5:
            rank5_items.append(item)


# main program

ITEM1 = 'N'
ITEM2 = 'M'
ITEM3 = 'R'
ITEM4 = 'L'
ITEM5 = 'A'

rank1_items = []
rank2_items = []
rank3_items = []
rank4_items = []
rank5_items = []

# set how many times of trial
N = 500000

mychest = create_chest()
open_chests(N)

# statistics
P1 = 0.638
P2 = 0.25
P3 = 0.1
P4 = 0.01
P5 = 0.002

p1 = len(rank1_items)/N
p2 = len(rank2_items)/N
p3 = len(rank3_items)/N
p4 = len(rank4_items)/N
p5 = len(rank5_items)/N

# comparing
print(f'Probability of normal item is {p1}, and the pre-setting is {P1}')
print(f'Probability of magic item is {p2}, and the pre-setting is {P2}')
print(f'Probability of rare item is {p3}, and the pre-setting is {P3}')
print(f'Probability of legendary item is {p4}, and the pre-setting is {P4}')
print(f'Probability of ancient legendary item is {p5}, and the pre-setting is {P5}')
