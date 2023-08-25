"""
Quiz 313
q4

A clothing store is preparing for promotion during winter holidays.
If a customer purchases 4 or more items at once, they will
receive a 40% discount. If a customer purchases 2 or more items,
they will receive a 20% discount. If a customer only purchases 1 item,
they will receive a 10% discount. Assuming that the average price of
the items is CAD $180, please design a program to automatically calculate
the before-tax subtotal for customers.

Please write a program to solve the above problem.
Hint:	Please save your code in the file naming as stem1401_quiz313_q4_yourname.py
"""

number_item = int(input("How many items did you buy"))
item_price = 180
percentage = number_item * 10
one_item = item_price - item_price / 100 * percentage
other_item = number_item * item_price - item_price / 100 * percentage


if 0 < number_item == 1:
    print(f"The price is {one_item}$")
elif 1 < number_item <= 2:
    print(f"The price is {other_item}$")
elif 2 < number_item <= 4:
    print(f"The price is {other_item}$")
