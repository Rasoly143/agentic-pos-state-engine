import json
import re


def extract_json_array(text: str):
    """
    Extract first JSON array found in model output.
    """

    # Remove markdown if present
    text = text.strip()

    # Remove ```json blocks
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # Find first JSON array
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON array found in model output")

    json_str = match.group(0)

    return json_str


def safe_parse_json_array(text: str):
    """
    Attempts to safely parse JSON array.
    """

    json_str = extract_json_array(text)

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        # Try basic repair: replace single quotes with double quotes
        json_str_fixed = json_str.replace("'", '"')
        return json.loads(json_str_fixed)
