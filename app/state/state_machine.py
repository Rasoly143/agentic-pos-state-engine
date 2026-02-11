from typing import Dict, Tuple


class OrderStateMachine:
    def __init__(self):
        # Key: (name, size)
        self.state: Dict[Tuple[str, str], Dict] = {}

    def add_item(self, name: str, size: str, quantity: int):
        key = (name, size)

        if key not in self.state:
            self.state[key] = {
                "quantity": quantity,
                "modifiers": set()
            }
        else:
            self.state[key]["quantity"] = quantity

    def remove_item(self, name: str, size: str):
        key = (name, size)
        if key in self.state:
            del self.state[key]

    def add_modifier(self, name: str, size: str, modifier: str):
        key = (name, size)
        if key in self.state:
            self.state[key]["modifiers"].add(modifier)

    def remove_modifier(self, name: str, size: str, modifier: str):
        key = (name, size)
        if key in self.state:
            self.state[key]["modifiers"].discard(modifier)

    def apply_actions(self, actions: list):
        for action in actions:
            action_type = action.get("action")

            if action_type == "add_item":
                self.add_item(
                    action["name"],
                    action["size"],
                    action["quantity"]
                )

            elif action_type == "update_quantity":
                self.add_item(
                    action["name"],
                    action["size"],
                    action["quantity"]
                )

            elif action_type == "remove_item":
                self.remove_item(
                    action["name"],
                    action["size"]
                )

            elif action_type == "add_modifier":
                self.add_modifier(
                    action["name"],
                    action["size"],
                    action["modifier"]
                )

            elif action_type == "remove_modifier":
                self.remove_modifier(
                    action["name"],
                    action["size"],
                    action["modifier"]
                )

    def get_state(self):
        return self.state
