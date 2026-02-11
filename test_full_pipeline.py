from app.state.state_machine import OrderStateMachine
from app.output.formatter import state_to_items_list, build_final_output
from app.pricing.price_engine import calculate_order_total


# Nightmare scenario:
# "Two Lattes… actually make that three.
# Add vanilla… wait, no vanilla.
# And a Croissant… actually scratch the Croissant."

actions = [
    {"action": "add_item", "name": "Latte", "size": "Grande", "quantity": 2},
    {"action": "update_quantity", "name": "Latte", "size": "Grande", "quantity": 3},
    {"action": "add_modifier", "name": "Latte", "size": "Grande", "modifier": "Vanilla Syrup"},
    {"action": "remove_modifier", "name": "Latte", "size": "Grande", "modifier": "Vanilla Syrup"},
    {"action": "add_item", "name": "Butter Croissant", "size": None, "quantity": 1},
    {"action": "remove_item", "name": "Butter Croissant", "size": None},
]

# 1️⃣ Apply state transitions
machine = OrderStateMachine()
machine.apply_actions(actions)

# 2️⃣ Convert state to competition item format
items = state_to_items_list(machine.get_state())

# 3️⃣ Calculate price
total_price = calculate_order_total(items)

# 4️⃣ Build final output
final_output = build_final_output(items, total_price)

print(final_output)
