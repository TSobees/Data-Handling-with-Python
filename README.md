# Student Score Analysis

[![Project checks](https://github.com/TSobees/Data-Handling-with-Python/actions/workflows/checks.yml/badge.svg)](https://github.com/TSobees/Data-Handling-with-Python/actions/workflows/checks.yml)

A portable pandas project that validates student-score CSVs, ranks students,
handles tied averages, and exports subject summaries. The included records are fictional.

## Run the example

Use Python 3.12 or 3.13 from the repository root:

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

This prints results and creates `outputs/student_rankings.csv` and
`outputs/subject_summary.csv`. Generated reports are ignored by Git.

## Analyze your CSV

```sh
python -m student_scores path/to/scores.csv --output-dir outputs/my-class
python -m student_scores path/to/scores.csv --subjects "Maths,English" --pass-mark 60
```

Every row needs a nonblank, unique `Name`. Selected subject scores must be
numeric, finite and between 0 and 100. Missing scores fail validation instead
of changing the number of subjects used in an average. Ties share the same
competition rank. All eleven default subjects are visible in
[the sample CSV](data/sample_scores.csv).

## Repository layout

```text
main.py                 Compatible launcher
student_scores/         Importable analysis functions and CLI
data/sample_scores.csv  Fictional runnable example
tests/                  Validation, tie and summary checks
.github/workflows/      Python 3.12 and 3.13 checks
```

## Tests and scope

```sh
python -m unittest discover -s tests -v
```

These are descriptive summaries; they do not measure teaching quality or
adjust scores for subject difficulty. Keep actual student records out of commits.
No reuse license has been added; the repository's original licensing choice is retained.

Author: Sobanjo Oluwatosin. AI assistance was used for the portability,
validation, exports, documentation and tests in this revision.
