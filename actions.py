from nemoguardrails.actions import action
import re

# ✅ Checks if input is related to Python coding using simple keywords and patterns
@action(name="is_coding_query")
async def is_coding_query(context: dict) -> bool:
    user_input = context.get("user_input", "").lower()

    trigger_phrases = [
        "python code", "python script", "python function",
        "write python", "generate python", "evaluate python",
        "check python", "modify python", "create python"
    ]

    # Keyword match
    if any(phrase in user_input for phrase in trigger_phrases):
        return True

    # Simple pattern match for pasted code
    if re.search(r"def\s+\w+\(", user_input) or re.search(r"import\s+\w+", user_input):
        return True

    return False

# ✅ Checks if input is too long
@action(name="max_length_check")
async def max_length_check(context: dict) -> bool:
    user_input = context.get("user_input", "")
    return len(user_input) <= 1000

# ✅ Dummy code generator (replace with LLM call later)
@action(name="generate_compliant_code")
async def generate_compliant_code(context: dict) -> str:
    return "def hello_world():\n    print('Hello, world!')"

# ✅ Basic compliance check for PEP-8 + PAC (placeholder logic)
@action(name="run_pep8_and_pac_check")
async def run_pep8_and_pac_check(context: dict, code: str) -> bool:
    return all([
        "def " in code,
        "print" in code or "return" in code,
        len(code) < 500
    ])

# ✅ Language detection based on common Python patterns
@action(name="detect_language")
async def detect_language(context: dict) -> str:
    user_input = context.get("user_input", "").lower()
    if "def " in user_input or "import " in user_input:
        return "Python"
    return "Unknown"
