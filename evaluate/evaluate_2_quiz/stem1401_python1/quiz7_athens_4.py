"""
Print out a real invoice

<<business concerns>>
text-based, command-line interface
not interaction (no user input)
layout - of equal width, limited width, 79 - 82 chars per line
take 80 chars per line
letter size
font - system font

layout - UI (user interface)
section 1:  header
line #1:    company name + title
line #2:    blank line X 1
line #3:    address line 1
line #4:    address line 2
line #5:    blank line X 4

section 2:  general info. of invoice
(business, logical)
block 1:    bill to
block 2:    ship to
block 3:    title of invoice info.
block 4:    value of invoice info.

(physical)
line #1:
line #2:
line #3:
line #4:
line #5:    blank line X 2

section 3:  details of item and summary
line of grid:  ---------------------   '-' X 80, x 5lines

grid:
line #1:    header of grid
line #2:    item info (qty, desc, unit_price, amount)
line #3:    item info
line #4:    item info

line #5:    subtotal (subtotal amount)
line #6:    tax (tax rate, tax amount)
line #7:    total


section 4:  footer
line #1:    title of terms
line #2:    statement of terms x 1
line #3:    blank line x 1
line #4:    comment or note x 1


<<technical concerns>>
print()
string formatting (alignment)  string_temp.format()
< = > %f %d
set variables, and naming
minimize the quantity of variable name
make them meaningful

<<data concerns>>
section 3. structured data
amount = qty x unit price
subtotal = amount1 + amount2 + amount3
tax amount = TAX_RATE x subtotal
total = subtotal + tax amount

<<optimization>>
minimize number of variables
outlook



date:   2021-07-05
author: Athens

step 1. analysis
step 2. plan
step 3. implementation (writing code)

"""

# global settings
# num of chars per line for printing
WIDTH = 80
BLANK = ''

# section 1. header
company_name = 'East Repair Inc.'
doc_title = 'INVOICE'
address_line1 ='1912 Harvest Lane'
address_line2 ='New York, NY 12210'

# line width = 70 chars + 10 chars
line1 = '{:70}{:>10}'.format(company_name, doc_title)
line3 = '{:80}'.format(address_line1)
line4 = '{:80}'.format(address_line2)

print(line1)
print(BLANK)
print(line3)
print(line4)
print(BLANK)
print(BLANK)
print(BLANK)
print(BLANK)

# section 2
# section 2-1
billto_title = 'Bill To'
billto_name='John Smith'
billto_address1= '2 Court Square'
billto_address2 = 'New York, NY 12210'

# section 2-2
shipto_title = 'Bill To'
shipto_name='John Smith'
shipto_address1= '2 Court Square'
shipto_address2 = 'New York, NY 12210'

# section 2-3
title_invoice_no = 'Invoice #'
title_invoice_date = 'Invoice Date'
title_po_no = 'P.O.#'
title_due_date = 'Due Date'

# section 2-4
value_invoice_no = 'US-001'
value_invoice_date = '11/02/2019'
value_po_no = '2313/2019'
value_due_date = '26/02/2019'

# contents of section 2
template2='{:25}{:20}{:>23}{:>12}'
line1 = template2.format(billto_title,shipto_title,title_invoice_no,value_invoice_no)
line2 = template2.format(billto_name,shipto_name,title_invoice_date,value_invoice_date)
line3 = template2.format(billto_address1,billto_address1,title_po_no,title_due_date)
line4 = template2.format(shipto_address1,shipto_address2,value_po_no,value_due_date)

print(line1)
print(line2)
print(line3)
print(line4)
print(BLANK)

# section 3
title_qty = 'QTY'
title_desc = 'DESCRIPTION'
title_unitprice = 'UNIT PRICE'
title_amount = 'AMOUNT'


# item data
items = [[1,'Front and rear brake cables',100.0,100.0],
         [2, 'New set of pedal arms',15.0,30.0],
         [3, 'Labor 3hrs', 5.0, 15.0],
         [4, 'Labor 3hrs', 5.0, 20.0]]

subtotal = items[0][3] + items[1][3] + items[2][3] + items[3][3]
TAX_RATE = 6.25*0.01
tax_amount = subtotal*TAX_RATE
total = subtotal + tax_amount

template3a = '{:^5}{:^40s}{:^15}{:^20}'
template3b = '{:^5}{:40}{:15.2f}{:20.2f}'
template3c = '{:>60}{:20.2f}'
template3d = '{:80}'
line_seg = '-'*80
LINE_SEP = template3d.format(line_seg)
line1 = template3a.format(title_qty,title_desc,title_unitprice,title_amount)
line2 = template3b.format(items[0][0], items[0][1], items[0][2], items[0][3])
line3 = template3b.format(items[1][0], items[1][1], items[1][2], items[1][3])
line4 = template3b.format(items[2][0], items[2][1], items[2][2], items[2][3])
line8 = template3b.format(items[3][0], items[3][1], items[3][2], items[3][3])

line5 = template3c.format('Subtotal',subtotal)
line6 = template3c.format('Sales Tax 6.25%',tax_amount)
line7 = template3c.format('Total',total)

print(LINE_SEP)
print(line1)
print(LINE_SEP)
print(line2)
print(LINE_SEP)
print(line3)
print(LINE_SEP)
print(line4)
print(LINE_SEP)
print(line8)
print(LINE_SEP)
print(line5)
print(line6)
print(line7)
print(BLANK)
print(BLANK)
print(BLANK)

# section 4 footer
term_title = 'Terms & Conditions'
term_1 = 'Payment is due within 15 days'
term_2 = 'Please make checks payable to:'+ company_name

print(term_title)
print(term_1)
print(BLANK)
print(term_2)
