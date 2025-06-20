# List of items, each item is a dictionary with price and quantity
items = [
    {"name": "Apples", "price": 2.5, "quantity": 4},
    {"name": "Bananas", "price": 1.2, "quantity": 6},
    {"name": "Milk", "price": 3.0, "quantity": 2},
    {"name": "Bread", "price": 2.0, "quantity": 1}
]

# Initialize total cost
total_cost = 0.0

# Calculate total cost
for item in items:
    item_total = item["price"] * item["quantity"]
    print(f"{item['name']}: ${item['price']} x {item['quantity']} = ${item_total:.2f}")
    total_cost += item_total

# Display the total bill
print(f"\nTotal Bill: ${total_cost:.2f}")
