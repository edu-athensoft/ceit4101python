"""
represent customer info with dictionary
"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is verified": True
}
print(customer)

# error
# print(customer["birthday"])

# None for undefined key
customer.get("birthday")
print(customer)
print(customer.get("birthday"))


#
print(customer.get("birthday","2020-03-12"))
print(customer)


# add a key-value pair
customer["birthday"]="2020-03-12"
print(customer)