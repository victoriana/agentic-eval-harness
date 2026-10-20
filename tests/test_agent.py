import os
from agentic_eval_harness.gemini_client import ask_ai
from dotenv import load_dotenv

load_dotenv()
# Key is now loaded from .env file automatically

# Test it
response = ask_ai("Say hello in exactly 3 words.")
print(response)