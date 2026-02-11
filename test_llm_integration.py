from app.parsing.llm_parser import LLMParser


# Simulated messy LLM output
def fake_model(system_prompt, user_input):
    return """
    Sure! Here's the structured result:

    ```json
    [
        {'action': 'add_item', 'name': 'Latte', 'size': 'Grande', 'quantity': 2},
        {'action': 'update_quantity', 'name': 'Latte', 'size': 'Grande', 'quantity': 3}
    ]
    ```
    """


parser = LLMParser(model_callable=fake_model)

actions = parser.parse("Two Lattes… actually make that three.")

print(actions)
