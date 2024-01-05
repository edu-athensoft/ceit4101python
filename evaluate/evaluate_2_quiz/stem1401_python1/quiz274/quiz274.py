"""
Quiz 274
Formatting - alignment

Formatting code for alignment
<, ^, >, =
"""

# 1. Please write the output of the given code snippet.
print("{:6d}".format(274))
print("{:>6d}".format(274))
print("{:^9.2f}".format(12.246))
print("{:<06d}".format(274))
print("{:=9.2f}".format(-12.246))


# 2. Please write the output of the given code snippet.
print("{:5}".format("bat"))
print("{:<5}".format("bat"))
print("{:>5}".format("bat"))
print("{:^5}".format("bat"))
print("{:*^5}".format("bat"))


# 3. Please write the output of the given code snippet.
print("{:.4}".format("examination"))
print("{:6.4}".format("examination"))
print("{:^6.4}".format("examination"))


# 4. Please write code to format dictionary members using format() and output exactly as given text content.
product = {'productId': 101, 'productName': 'Mouse', 'unitPrice': 79.99, 'qty': 2, 'amount': 159.98}

"""
The expected output is as follows:
The product information is product id : 101, product name : Mouse, unit price : $79.99, 
quantity : 2, amount: $159.98 .
"""

print("The product information is product id : {p[productId]}, product name : {p[productName]}, "
      "unit price : {p[unitPrice]}, quantity : {p[qty]}, amount: ${p[amount]} .".format(p=product))







