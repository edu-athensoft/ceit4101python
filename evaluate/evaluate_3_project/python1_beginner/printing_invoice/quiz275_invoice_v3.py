"""
Project/Quiz 275: Printing Invoice
version: 3

extracting string templates

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
# data 3x3 grid
items = [[1, "Front and rear brake cables", 100.00],
    [2, "New set of pedal arms", 15.00],
    [3, "Labor 3hrs", 5.00],
    [4, "Service 1", 8.00]]

subtotal = items[0][0] * items[0][2] + \
           items[1][0] * items[1][2] + \
           items[2][0] * items[2][2] + \
           items[3][0] * items[3][2]

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
print(item_template.format(items[0][0], items[0][1], items[0][2], items[0][0] * items[0][2]))
print(item_template.format(items[1][0], items[1][1], items[1][2], items[1][0] * items[1][2]))
print(item_template.format(items[2][0], items[2][1], items[2][2], items[2][0] * items[2][2]))
print(item_template.format(items[3][0], items[3][1], items[3][2], items[3][0] * items[3][2]))

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