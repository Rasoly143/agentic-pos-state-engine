from app.pricing.price_engine import calculate_item_price, calculate_order_total


# Test 1: Simple Latte, Grande, no modifiers
item1 = {
    "name": "Latte",
    "size": "Grande",
    "quantity": 1,
    "modifiers": []
}

print("Test 1:", calculate_order_total([item1]))
# Expected: 4.50 + 0.50 = 5.00


# Test 2: 3 Venti Mochas with Oat Milk
item2 = {
    "name": "Mocha",
    "size": "Venti",
    "quantity": 3,
    "modifiers": ["Oat Milk"]
}

print("Test 2:", calculate_order_total([item2]))
# Expected:
# Base 5.00
# + Size 1.00
# + Oat 0.80
# = 6.80 per unit
# 6.80 * 3 = 20.40


# Test 3: Latte with 2 syrups stacking
item3 = {
    "name": "Latte",
    "size": "Tall",
    "quantity": 1,
    "modifiers": ["Vanilla Syrup", "Caramel Syrup"]
}

print("Test 3:", calculate_order_total([item3]))
# Expected:
# 4.50 + 0.00 + 0.50 + 0.50 = 5.50


# Test 4: Multi-item order
order = [
    {
        "name": "Latte",
        "size": "Grande",
        "quantity": 2,
        "modifiers": ["Oat Milk"]
    },
    {
        "name": "Butter Croissant",
        "size": None,
        "quantity": 1,
        "modifiers": []
    }
]

print("Test 4:", calculate_order_total(order))
# Expected:
# Latte: (4.50 + 0.50 + 0.80) = 5.80 * 2 = 11.60
# Croissant: 3.50
# Total = 15.10
