from app.parsing.mock_parser import MockLLMParser
from app.state.state_machine import OrderStateMachine
from app.output.formatter import state_to_items_list, build_final_output
from app.pricing.price_engine import calculate_order_total


# Simulated customer order
order_text = "Two Lattes… actually make that three."

# 1️⃣ Parse order into structured actions
parser = MockLLMParser()
actions = parser.parse(order_text)

# 2️⃣ Apply actions to state machine
machine = OrderStateMachine()
machine.apply_actions(actions)

# 3️⃣ Convert state to competition format
items = state_to_items_list(machine.get_state())

# 4️⃣ Calculate pricing
total_price = calculate_order_total(items)

# 5️⃣ Build final JSON
final_output = build_final_output(items, total_price)

print(final_output)
