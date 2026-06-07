# The General Knowledge Quiz

A small CLI quiz game that asks general knowledge questions, scores your answers, and shows a final summary.

## How to Run

```bash
python main.py
```

## How It Works

- Asks a series of questions in random order
- Sanitizes input (trims whitespace and normalizes case)
- Scores +1 for each correct answer
- Prints a final score and any missed questions

## Customize Questions

Edit the `questions` list in `main.py` to add, remove, or change prompts and answers.
