from z_debuggers import ruler, banner

fruits_inventory = [
    {"name": "apple", "quantity": 10, "price_per_kg": 120},  # 0
    {"name": "banana", "quantity": 25, "price_per_kg": 60},  # 1
    {"name": "orange", "quantity": 8, "price_per_kg": 100},  # 2
    {"name": "grapes", "quantity": 30, "price_per_kg": 90},  # 3
    {"name": "watermelon", "quantity": 4, "price_per_kg": 40},  # 4
]

"""
Practice Ideas
    You can try:
        - Creating a new list of fruits with quantity less than 15
        - Creating a new list with only the name and total value (quantity * price_per_kg)
        - Filtering fruits that cost more than 100 per kg
"""

banner("Create a new list of fruits where quantity < 15")
low_quantity_fruits = [] # empty list to store the fruits
for fruits_q in fruits_inventory:
    if fruits_q["quantity"] < 15:
        low_quantity_fruits.append(fruits_q)

print("These are the low quantity fruits: ")
for fruit in low_quantity_fruits:
    print(fruit["name"])
ruler()

banner("Create a new list with only the name and total value")
name_and_total_value = [] # empty list
index = 1
for fruits_t in fruits_inventory:
    total_value = fruits_t["quantity"] * fruits_t["price_per_kg"]
    new_entry = {
        "name": fruits_t["name"],
        "total_value": total_value
    }
    index += 1
    name_and_total_value.append(new_entry)

print("\nFruits and their total value: ")
for fruit in name_and_total_value:
    print(f"{fruit['name']} - {fruit['total_value']}")

banner("Filtering fruits that cost more than 100 per kg")
expensive_fruits = []
for fruits in fruits_inventory:
    if fruits["price_per_kg"] > 100:
        expensive_fruits.append(fruits)

print("\nFruits that cost more than 100 per kg: ")
for fruit in expensive_fruits:
    print(fruit['name'])
ruler()

banner("using list comprehension")
low_stock_fruits = [fruit for fruit in fruits_inventory if fruit["quantity"] < 15]
name_and_values = [
    {"name": fruit["name"], "total_value": fruit["quantity"] * fruit["price_per_kg"]}
    for fruit in fruits_inventory
]
expensive_fruits = [fruit for fruit in fruits_inventory if fruit["price_per_kg"] > 100]

print(f"Low stock fruits: ")
for stock in low_stock_fruits:
    print(f"{stock['name']} - {stock['quantity']}")
ruler()

print(f"Fruits with their total value: ")
for t_value in name_and_values:
    print(f"{t_value['name']} - {t_value['total_value']}")

ruler()
print(f"Expensive fruits are: ")
for expensive in expensive_fruits:
    print(f"{expensive['name']} - {expensive["price_per_kg"]}")
