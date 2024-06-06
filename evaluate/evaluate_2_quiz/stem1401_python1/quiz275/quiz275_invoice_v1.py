"""
Project/Quiz 275: Printing Invoice
version: 1

setting and naming variables
formatting
"""

# header
print()
print()
print("{:76}{:>12}".format("East Repair Inc.", "INVOICE"))
print()
print("{}".format("1912 Harvest Lane"))
print("{}".format("New York, NY 12210"))


# basic info
print()
print()
print()
print("{:28}{:35}{:19}{}".format("Bill To", "Ship To", "Invoice #", "US-001"))
print("{:28}{:32}{:18}{}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print("{:28}{:39}{:12}{}".format("2 Court Square", "37B7 Pineview Drive", "P.O.#", "2312/2019"))
print("{:28}{:36}{:14}{}".format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))
print()
print()


# detail
# data
qty1 = 1
qty2 = 2
qty3 = 3

price1 = 100.00
price2 = 15.00
price3 = 5.00

amount1 = qty1 * price1
amount2 = qty2 * price2
amount3 = qty3 * price3

subtotal = amount1 + amount2 + amount3
sales_tax = 6.25/100
tax_amount = subtotal * sales_tax
total = subtotal + tax_amount

# data grid for items
line_template = "{:88}"
print(line_template.format('-'*88))
head_template = "{:^7}{:^39}{:^20}{:^22}"
print(head_template.format("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT"))
print(line_template.format('-'*88))

item_template = "{:^7}{:<39}{:>20}{:>22}"
print(item_template.format(qty1, "Front and rear brake cables", price1, amount1))
print(item_template.format(qty2, "New set of pedal arms", price2, amount2))
print(item_template.format(qty3, "Labor 3hrs", price3, amount3))

print(line_template.format('-'*88))

# summary
sumary_template = "{:>66}{:>22.2f}"
print(sumary_template.format("Subtotal", subtotal))
print(sumary_template.format("Sales Tax 6.25%", tax_amount))
print(sumary_template.format("TOTAL", total))
print()
print()

# terms
print("{}".format("Terms & Conditions"))
print("{}".format("Payment is due within 15 days"))
print()
print("{}".format("Please make checks payable to: East Repair Inc."))
print()
print()