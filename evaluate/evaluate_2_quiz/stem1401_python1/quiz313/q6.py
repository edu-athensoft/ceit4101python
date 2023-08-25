"""
Quiz 313
q6

A computer game company is developing a 3A-level role-playing game.
The character you are controlling will receive equipment items of
different tiers while adventuring in the big world. The system will
display different background and text colors according to the level
of the item to distinguish them. If the item is of the first tier,
the system uses gray; if the item is of the second tier, the system
uses green; if the item is of the tier level, the system uses blue;
if the item is of the fourth tier, the system uses purple; if the item
is of the fifth tier, the system uses gold(en).

Please write a program to determine what color should be used to
display the background and text of an item based on its tier when
you pick up an item and know its tier number.

Hint:	Please save your code in the file naming as stem1401_quiz313_q6_yourname.py
"""

# tier numbers = 1, 2, 3, 4, 5

tier_num = int(input("Input a number of tier: "))

color = None

if tier_num == 1:
    color = "gray"
elif tier_num == 2:
    color = "green"
elif tier_num == 3:
    color = "blue"
elif tier_num == 4:
    color = "purple"
elif tier_num == 5:
    color = "golden"
else:
    print("Invalid input.")

if color:
    print(f"The right color of tier number {tier_num} should be {color}.")
