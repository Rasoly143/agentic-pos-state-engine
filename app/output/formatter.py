def state_to_items_list(state_dict: dict):
    """
    Convert internal state machine dict to competition-required list format.
    """

    items = []

    for (name, size), data in state_dict.items():
        items.append({
            "name": name,
            "size": size,
            "quantity": data["quantity"],
            "modifiers": list(data["modifiers"])
        })

    return items


def build_final_output(items: list, total_price: float):
    """
    Build final JSON output structure.
    """

    return {
        "items": items,
        "total_price": round(total_price, 2)
    }
