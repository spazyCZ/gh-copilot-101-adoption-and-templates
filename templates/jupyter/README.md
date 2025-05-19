# Jupyter Template for Project Use

This folder provides a starting point for Jupyter-based projects. Please follow these best practices:

## Best Practices for Jupyter Projects
- Use [seaborn](https://seaborn.pydata.org/) and [matplotlib](https://matplotlib.org/) for all visualizations to ensure standardized, publication-quality charts.
- Use Python's `logging` module for event and error reporting, not print statements.
- Annotate all functions with type hints and docstrings.
- Place all reusable code in separate `.py` modules and import them into notebooks.
- Document all steps and code cells with markdown and comments.
- Use `pytest` for any testable logic in `.py` modules.
- Keep notebooks clean: restart and run all cells before committing.

## Example Structure
- `notebooks/` — Jupyter notebooks for analysis and reporting
- `src/` — Python modules for reusable logic
- `tests/` — Unit tests for modules
- `.vscode/` — Recommended VS Code settings and extensions

## Required Extensions
See `.vscode/extensions.json` for recommended VS Code extensions for Jupyter development.

## Example Notebook
- `example_analysis.ipynb`: Example notebook with best practices for data analysis and visualization.
- `src/utils.py`: Utility functions for use in notebooks (logging, summaries, etc).
