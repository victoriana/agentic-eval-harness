# Agentic Eval Harness

A lightweight evaluation harness for agentic AI systems. This project provides a framework to test agent accuracy, latency, and governance compliance against a golden dataset.

## Purpose
As AI agents become more complex, ensuring they operate within defined policy boundaries and maintain accuracy is critical. This harness allows developers to:
- Run agents against curated question-answer pairs.
- Measure exact and fuzzy match accuracy.
- Audit output for PII leakage or policy violations.

## Status
This is the foundational repo for the 12-week GitHub Staff preparation plan. It will evolve into a full-featured evaluation tool with CI-gated accuracy thresholds.

## Architecture
- **Agent:** LangGraph with Bedrock Claude
- **Eval Logic:** Python-based scorer
- **Governance:** Input sanitization and PII filtering via regex/NER

## Related
- [acrochoreo](https://github.com/victoriana/acrochoreo) — supervisor graph orchestrator (evaluation target)
- [github-actions-reusable-workflow](https://github.com/victoriana/github-actions-reusable-workflow) — CI governance template
