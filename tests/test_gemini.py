from agentic_eval_harness.gemini_client import ask_ai

def test_ask_ai_returns_nonempty():
    response = ask_ai("Say hello in exactly 3 words.")
    assert len(response.strip().split()) == 3
    assert "hello" in response.lower() or "hi" in response.lower()