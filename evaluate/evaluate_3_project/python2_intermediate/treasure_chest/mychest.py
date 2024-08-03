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
    list1 = [ITEM1] * 638
    list2 = [ITEM2] * 250
    list3 = [ITEM3] * 100
    list4 = [ITEM4] * 10
    list5 = [ITEM5] * 2

    chests = list1 + list2 + list3 + list4 + list5

    random.shuffle(chests)
    return chests


# trials
def open_chests(t, from_chests):
    def get_item(chests):
        return random.choice(chests)

    rank1_items = []
    rank2_items = []
    rank3_items = []
    rank4_items = []
    rank5_items = []

    for i in range(t):
        item = get_item(from_chests)

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

    return {
        "rank1_items": rank1_items,
        "rank2_items": rank2_items,
        "rank3_items": rank3_items,
        "rank4_items": rank4_items,
        "rank5_items": rank5_items,
    }



def main(times=500000):
    # 1. create all chests

    all_chests = create_chest()

    # 2. open chests
    # set how many times of trial
    N = times
    items_by_rank_dict = open_chests(N, all_chests)

    # 3. get real probabilities
    # pre-setting probabilities for items of each item
    P1 = 0.638
    P2 = 0.25
    P3 = 0.1
    P4 = 0.01
    P5 = 0.002

    p1 = len(items_by_rank_dict['rank1_items'])/N
    p2 = len(items_by_rank_dict['rank2_items'])/N
    p3 = len(items_by_rank_dict['rank3_items'])/N
    p4 = len(items_by_rank_dict['rank4_items'])/N
    p5 = len(items_by_rank_dict['rank5_items'])/N


    # 4. Output to compare real probabilities with pre-setting probabilities
    print(f"{N:,} times of trial")
    category_width = 9  # max width

    print(f'Probability of {"normal":<{category_width}} item is {p1:.4f}, and the pre-setting is {P1:.4f}, Diff is {p1-P1:>7.4f}')
    print(f'Probability of {"magic":<{category_width}} item is {p2:.4f}, and the pre-setting is {P2:.4f}, Diff is {p2-P2:>7.4f} ')
    print(f'Probability of {"rare":<{category_width}} item is {p3:.4f}, and the pre-setting is {P3:.4f}, Diff is {p3-P3:>7.4f} ')
    print(f'Probability of {"legendary":<{category_width}} item is {p4:.4f}, and the pre-setting is {P4:.4f}, Diff is {p4-P4:>7.4f} ')
    print(f'Probability of {"ancient":<{category_width}} item is {p5:.4f}, and the pre-setting is {P5:.4f}, Diff is {p5-P5:>7.4f} ')
    print()

# settings
ITEM1 = 'N'
ITEM2 = 'M'
ITEM3 = 'R'
ITEM4 = 'L'
ITEM5 = 'A'

# main program
main(10000)
main(100000)
main(500000)
main(1000000)
main(5000000)
