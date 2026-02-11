from app.parsing.prompt_template import SYSTEM_PROMPT
from app.parsing.json_utils import safe_parse_json_array
from app.parsing.action_validator import validate_action_list


class LLMParser:
    """
    Real parser abstraction.
    Later will integrate actual LLM inference.
    """

    def __init__(self, model_callable=None):
        """
        model_callable: function that takes (system_prompt, user_input)
        and returns raw model output string.
        """
        self.model_callable = model_callable

    def parse(self, order_text: str):
        if self.model_callable is None:
            raise RuntimeError("No model callable provided.")

        # 1️⃣ Call model
        raw_output = self.model_callable(SYSTEM_PROMPT, order_text)

        # 2️⃣ Extract + repair JSON
        actions = safe_parse_json_array(raw_output)

        # 3️⃣ Validate schema
        validate_action_list(actions)

        return actions
