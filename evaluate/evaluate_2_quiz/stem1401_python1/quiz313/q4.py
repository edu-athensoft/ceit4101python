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
discount_1 = 0.1
discount_2 = 0.2
discount_4 = 0.4

subtotal = 0
if 0 < number_item == 1:
    subtotal = number_item * item_price * (1-discount_1)
elif 1 < number_item <= 2:
    subtotal = number_item * item_price * (1-discount_2)
elif 2 < number_item <= 4:
    subtotal = number_item * item_price * (1-discount_4)

# subtotal
print(f"The subtotal before tax is ${subtotal:.2f}")