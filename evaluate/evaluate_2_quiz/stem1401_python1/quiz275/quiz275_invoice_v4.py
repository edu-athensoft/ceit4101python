"""
Project/Quiz 275: Printing Invoice
version: 4

optimizing
separating layout from logic
"""

# settings
# general settings
DOC_WIDTH = 88
LINE_CHAR = '~'

# invoice layout
invoice_head_template = "{:76}{:>12}"

basic_info_1_template = "{:28}{:35}{:19}{}"
basic_info_2_template = "{:28}{:32}{:18}{}"
basic_info_3_template = "{:28}{:39}{:12}{}"
basic_info_4_template = "{:28}{:36}{:14}{}"

line_template = "{:88}"
grid_head_template = "{:^7}{:^39}{:^20}{:^22}"
item_template = "{:^7}{:<39}{:>20}{:>22}"
summary_template = "{:>66}{:>22.2f}"

# default values
SUMMARY_SUBTOTAL = "Subtotal"
SUMMARY_TAX = "Sales Tax 6.25%"
SUMMARY_TOTAL= "TOTAL"

SALES_TAX_RATE = 6.25
# TERMS_TITLE = "Terms & Conditions"
# TERMS_LINE_1 = "Payment is due within 15 days"
# TERMS_LINE_2 = "Please make checks payable to: East Repair Inc."

TERMS_TITLE = "Conditions générales"
TERMS_LINE_1 = "Payment is due within 15 days"
TERMS_LINE_2 = "Please make checks payable to: East Repair Inc."

# header
print()
print()
print(invoice_head_template.format("East Repair Inc.", "INVOICE"))
print()
print("{}".format("1912 Harvest Lane"))
print("{}".format("New York, NY 12210"))


# basic info
print()
print()
print()
print(basic_info_1_template.format("Bill To", "Ship To", "Invoice #", "US-001"))
print(basic_info_2_template.format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print(basic_info_3_template.format("2 Court Square", "37B7 Pineview Drive", "P.O.#", "2312/2019"))
print(basic_info_4_template.format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))
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

sales_tax = SALES_TAX_RATE/100
tax_amount = subtotal * sales_tax
total = subtotal + tax_amount

# data grid for items
print(line_template.format(LINE_CHAR*DOC_WIDTH))
print(grid_head_template.format("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT"))
print(line_template.format(LINE_CHAR*DOC_WIDTH))


print(item_template.format(items[0][0], items[0][1], items[0][2], items[0][0] * items[0][2]))
print(item_template.format(items[1][0], items[1][1], items[1][2], items[1][0] * items[1][2]))
print(item_template.format(items[2][0], items[2][1], items[2][2], items[2][0] * items[2][2]))
print(item_template.format(items[3][0], items[3][1], items[3][2], items[3][0] * items[3][2]))

print(line_template.format(LINE_CHAR*DOC_WIDTH))

# summary
print(summary_template.format(SUMMARY_SUBTOTAL, subtotal))
print(summary_template.format(SUMMARY_TAX, tax_amount))
print(summary_template.format(SUMMARY_TOTAL, total))
print()
print()

# terms
print("{}".format(TERMS_TITLE))
print("{}".format(TERMS_LINE_1))
print()
print("{}".format(TERMS_LINE_2))
print()
print()