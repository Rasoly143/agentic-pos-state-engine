VALID_ACTIONS = {
    "add_item",
    "update_quantity",
    "remove_item",
    "add_modifier",
    "remove_modifier"
}


def validate_action(action: dict):
    if "action" not in action:
        raise ValueError("Missing 'action' key")

    if action["action"] not in VALID_ACTIONS:
        raise ValueError(f"Invalid action type: {action['action']}")

    # Required fields depending on action type
    action_type = action["action"]

    if action_type in {"add_item", "update_quantity"}:
        required = {"name", "size", "quantity"}
    elif action_type == "remove_item":
        required = {"name", "size"}
    elif action_type in {"add_modifier", "remove_modifier"}:
        required = {"name", "size", "modifier"}
    else:
        required = set()

    missing = required - action.keys()
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    return True


def validate_action_list(actions: list):
    if not isinstance(actions, list):
        raise ValueError("Actions must be a list")

    for action in actions:
        validate_action(action)

    return True
