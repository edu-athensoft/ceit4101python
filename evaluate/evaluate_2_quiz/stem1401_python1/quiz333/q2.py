"""
q2.
Write a Python program to calculate the total revenue for each product and
the overall total revenue for the store.
"""

# Sales data
sales_data = [
    {"product": "Apple", "quantity": 50, "price_per_unit": 0.5},
    {"product": "Banana", "quantity": 100, "price_per_unit": 0.2},
    {"product": "Orange", "quantity": 70, "price_per_unit": 0.3},
]

# Initialize total revenue
total_revenue = 0

# Loop through each product and calculate total revenue
for sale in sales_data:
    product = sale["product"]
    quantity = sale["quantity"]
    price_per_unit = sale["price_per_unit"]

    # Calculate revenue for this product
    product_revenue = quantity * price_per_unit
    total_revenue += product_revenue

    # Print the revenue for this product
    print(f"{product}: ${product_revenue:.1f}")

# Print the overall total revenue
print(f"Total Revenue: ${total_revenue:.1f}")
