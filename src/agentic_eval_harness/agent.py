import csv
from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END

from agentic_eval_harness.gemini_client import ask_ai


class EvalState(TypedDict):
    data_path: str
    questions: List[str]
    golden_answers: List[str]
    current_index: int
    results: List[Dict]


def load_context(state: EvalState) -> EvalState:
    questions, answers = [], []
    with open(state["data_path"], newline="") as f:
        for row in csv.DictReader(f):
            questions.append(row["question"])
            answers.append(row["answer"])
    return {**state, "questions": questions, "golden_answers": answers}


def run_evaluation(state: EvalState) -> EvalState:
    i = state["current_index"]
    question = state["questions"][i]
    expected = state["golden_answers"][i]

    actual = ask_ai(question)
    correct = expected.lower() in actual.lower()

    results = state["results"] + [
        {"question": question, "expected": expected, "actual": actual, "correct": correct}
    ]
    return {**state, "current_index": i + 1, "results": results}


def should_continue(state: EvalState) -> str:
    return "continue" if state["current_index"] < len(state["questions"]) else "done"


workflow = StateGraph(EvalState)
workflow.add_node("loader", load_context)
workflow.add_node("evaluator", run_evaluation)
workflow.set_entry_point("loader")
workflow.add_edge("loader", "evaluator")
workflow.add_conditional_edges("evaluator", should_continue, {"continue": "evaluator", "done": END})

app = workflow.compile()


def run_eval(data_path: str = "data.csv") -> Dict:
    final = app.invoke({
        "questions": [], "golden_answers": [],
        "current_index": 0, "results": [],
    })
    total = len(final["results"])
    score = sum(r["correct"] for r in final["results"]) / total if total else 0
    return {"accuracy": round(score, 2), "details": final["results"]}