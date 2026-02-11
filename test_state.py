from app.state.state_machine import OrderStateMachine


actions = [
    {"action": "add_item", "name": "Latte", "size": "Grande", "quantity": 2},
    {"action": "update_quantity", "name": "Latte", "size": "Grande", "quantity": 3},
    {"action": "add_modifier", "name": "Latte", "size": "Grande", "modifier": "Vanilla"},
    {"action": "remove_modifier", "name": "Latte", "size": "Grande", "modifier": "Vanilla"},
    {"action": "add_item", "name": "Croissant", "size": None, "quantity": 1},
    {"action": "remove_item", "name": "Croissant", "size": None},
]

machine = OrderStateMachine()
machine.apply_actions(actions)

print(machine.get_state())
