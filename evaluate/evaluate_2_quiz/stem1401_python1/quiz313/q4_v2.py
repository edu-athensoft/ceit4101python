"""
Quiz 313
q4
v2

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

print("=== Checking out ===")
number_item = int(input("How many items will you buy? "))

item_price = 180
DISCOUNT_FOR_4 = 0.4
DISCOUNT_FOR_2 = 0.2
DISCOUNT_FOR_1 = 0.1

subtotal = 0
message = None
discount = 0

if number_item >=4:
    discount = DISCOUNT_FOR_4
    subtotal = number_item * item_price * (1 - discount)
elif number_item >= 2:
    discount = DISCOUNT_FOR_2
    subtotal = number_item * item_price * (1 - discount)
elif number_item == 1:
    discount = DISCOUNT_FOR_1
    subtotal = number_item * item_price * (1 - discount)
else:
    message = "No purchase."

if subtotal > 0:
    message = f"Qty: {number_item}\nUnit price: ${item_price:.2f} CAD\nDiscount: {discount:.1%}\n"
    message += f'Subtotal: ${subtotal:.2f} CAD'

print("\n=== Summary ===")
print(message)
print("Thank you!")