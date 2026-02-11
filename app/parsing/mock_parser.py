from app.parsing.action_validator import validate_action_list


class MockLLMParser:
    """
    Simulates LLM parsing output.
    Used for pipeline testing before real model integration.
    """

    def parse(self, order_text: str):
        # Simple hardcoded example logic
        # Later replaced with real LLM inference

        if "Latte" in order_text:
            actions = [
                {"action": "add_item", "name": "Latte", "size": "Grande", "quantity": 2},
                {"action": "update_quantity", "name": "Latte", "size": "Grande", "quantity": 3},
            ]
        else:
            actions = []

        # Validate before returning
        validate_action_list(actions)

        return actions
