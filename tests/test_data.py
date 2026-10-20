from agentic_eval_harness.agent import load_context

def test_real_data_csv_parses():
    state = {"data_path": "data.csv", "questions": [], "golden_answers": [],
             "current_index": 0, "results": []}
    out = load_context(state)
    assert len(out["questions"]) == 5
    assert "Paris" in out["golden_answers"]