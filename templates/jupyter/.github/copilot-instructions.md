# Copilot Instructions for Jupyter Notebooks

## Table of Contents

* [Introduction](#introduction)
* [Key Objectives](#key-objectives)
* [Core Guidelines](#core-guidelines)
  * [Documentation Standards](#1-documentation-standards)
  * [Type Safety](#2-type-safety)
  * [Logging Standards](#3-logging-standards)
  * [Environment Configuration](#4-environment-configuration)
  * [Package Management](#5-package-management)
* [Jupyter Notebook Output Best Practices](#jupyter-notebook-output-best-practices)
  * [Simple Output](#simple-output)
  * [Table Output](#table-output)
  * [General Tips](#general-tips)
* [Markdown Best Practices](#markdown-best-practices)
* [Visualization Standards](#visualization-standards)
* [Testing in Notebooks](#testing-in-notebooks)
* [Coding Style and Best Practices](#coding-style-and-best-practices)
* [Reproducibility Best Practices](#reproducibility-best-practices)
* [Conclusion](#conclusion)

## Introduction

These guidelines streamline GitHub Copilot usage **inside Jupyter Notebooks**. They focus on readability, reproducibility, and safe interaction with external services while keeping notebooks easy to review and share.

## Key Objectives

✓ Generate clear, maintainable notebook code
✓ Provide thorough inline documentation and type‐hints
✓ Keep notebooks deterministic and reproducible
✓ Make every significant step self‑explanatory

## Core Guidelines

### 1. Documentation Standards

Add descriptive docstrings to every public function or class **inside code cells**.

```python
class DataProcessor:
    """
    Process data according to configured rules.

    Attributes
    ----------
    config : dict
        Configuration parameters for the processor.
    """

    def __init__(self, config: dict) -> None:
        """Create a new processor.

        Parameters
        ----------
        config : dict
            Dictionary containing configuration parameters.
        """
        self.config = config
```

### 2. Type Safety

Declare parameter and return types:

```python
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b
```

If you define metrics, subclass a shared `Metric` base class:

```python
class CustomMetric(Metric):
    def calculate(self) -> float:  # type: ignore[override]
        ...
```

### 3. Logging Standards

Use `logging` instead of `print` for informational messages.

```python
import logging, sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout,
    force=True,  # reset handlers added in the same kernel session
)
logger = logging.getLogger(__name__)
```

### 4. Environment Configuration

Load secrets and environment variables from a `.env` file rather than hard‑coding.

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ["MY_SERVICE_API_KEY"]
```

### 5. Package Management
- Include a `requirements.txt` file with all dependencies and their versions.
- Add a setup cell at the beginning of the notebook to install required packages using the Jupyter magic command:
  ```python
  # Install required packages
  %pip install pandas>=1.5.0 numpy>=1.22.0 matplotlib>=3.5.0 seaborn>=0.12.0
  
  # Alternatively, install from requirements.txt
  %pip install -r requirements.txt
  ```
- Always specify version requirements to ensure reproducibility.
- The `%pip` magic command is preferred over other approaches as it's specifically designed for Jupyter notebooks.
- Comment the installation cell if targeting environments where pip installs are not allowed.

## Jupyter Notebook Output Best Practices

### Simple Output

Use `print()` for short messages or single values.

```python
print("Processing completed.")
print(f"Number of rows: {len(df)}")
```

### Table Output

Prefer `IPython.display.display` for rich objects.

```python
from IPython.display import display

display(df.head(10))
```

Direct DataFrame evaluation at the end of a cell is acceptable:

```python
df.head(10)
```

For styled output:

```python
display(
    df.style.set_caption("Sample Data").highlight_max(axis=0)
)
```

### General Tips

* **Limit large outputs**: show only the needed rows/columns (`df.head()` or `df.sample(5)`).
* **Keep results deterministic**: set random seeds (`numpy.random.seed`, `random.seed`).
* **One logical action per cell**: split your workflow so that each cell performs a single well‑defined step (e.g. imports, data‑loading, cleaning, feature engineering, modelling, visualisation). This makes it easy to re‑run or debug a specific part without side‑effects.
* **Group related cells** with clear markdown headings (or Jupyter *cell tags*) so that collaborators can jump straight to the section they need.

## Markdown Best Practices

### Structure
* Use hierarchical heading levels (H1 for notebook title, H2 for major sections, H3 for subsections)
* Include a table of contents for longer notebooks
* Add section navigation links in longer notebooks

### Content
* Start with a clear title and introduction that states the notebook's purpose
* Explain the "why" behind analyses, not just the "how"
* Document assumptions and limitations
* Include conclusions and next steps at the end
* Use bullet points and numbered lists for better readability

### Formatting
* Use bold and italics for emphasis, not for all text
* Insert horizontal rules (`---`) to clearly separate major sections
* Format code references with backticks: `variable_name`
* Include citations and references where appropriate

### Media
* Include relevant images, diagrams, and charts with descriptive captions
* Use LaTeX for mathematical formulas: $y = mx + b$
* Embed links to external resources and documentation

## Visualization Standards

### General Principles
* Every visualization should have a clear title and labeled axes
* Include units of measurement where applicable
* Use colorblind-friendly palettes
* Add legends when using multiple colors or markers
* Maintain consistent styling across related visualizations

### Code Structure
```python
def create_visualization(data, **kwargs):
    """
    Create a standard visualization with proper labels and styling.
    
    Parameters
    ----------
    data : DataFrame
        The data to visualize
    **kwargs : dict
        Additional parameters for customization
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure object
    """
    # Create the visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot data
    sns.lineplot(data=data, x='x_column', y='y_column', ax=ax)
    
    # Add title and labels
    ax.set_title('Descriptive Title', fontsize=16)
    ax.set_xlabel('X Axis Label (units)', fontsize=12)
    ax.set_ylabel('Y Axis Label (units)', fontsize=12)
    
    # Add grid and styling
    ax.grid(True, linestyle='--', alpha=0.7)
    
    return fig
```

### Tools and Libraries
* Use Matplotlib for basic plots and fine-grained control
* Use Seaborn for statistical visualizations
* Use Plotly for interactive visualizations
* Consider Bokeh or Altair for complex interactive dashboards

### Best Practices
* Limit the number of elements in a single visualization
* Use faceting/small multiples for comparing across categories
* Choose appropriate chart types for your data
* Add context with annotations and reference lines
* Include source information and date of data collection

## Testing in Notebooks

For prototyping in Jupyter, use lightweight validation rather than formal unit tests:

### Assertion-Based Validation

```python
# Validate function behavior with assertions
def process_data(df):
    # processing logic
    return processed_df
    
result = process_data(sample_df)
assert result.shape[0] > 0, "Output DataFrame should not be empty"
assert "important_column" in result.columns, "Missing required column"
```

### Test Cells

Create dedicated cells for quick function validation with sample inputs:

```python
# TEST CELL: Verify data processing function
test_input = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
expected_cols = ["A", "B", "A_normalized", "B_normalized"]
result = normalize_features(test_input)
print(f"Output shape: {result.shape}, Expected columns exist: {all(col in result for col in expected_cols)}")
```

## Coding Style and Best Practices

### Cell Organization
* Organize notebook cells in a logical progression (imports → data loading → exploration → analysis → visualization → conclusion)
* Keep cells focused on a single task
* Keep code cells short and focused (<15 lines per cell when possible)
* Avoid mixing unrelated operations in a single cell
* Use descriptive markdown headings between logical sections
* Place imports in a dedicated cell at the beginning
* Include checkpoint cells that save intermediate results for long operations
* Ensure the notebook can run from top to bottom without errors
* Add cell tags when needed for cell execution control or slideshow formatting

### Code Quality
* Prefer functions over repeated code blocks
* Keep function definitions at the top of notebooks
* Use consistent variable naming (snake_case for variables, CamelCase for classes)
* Add comments for complex algorithms or calculations

### Performance
* Use vectorized operations when working with pandas/numpy
* Avoid loops for operations that can be vectorized
* Use appropriate data structures for the task (e.g., dictionaries for lookups)
* Consider using more efficient alternatives (e.g., pandas query() instead of boolean indexing for large datasets)

### Memory Management
* Use `del` to remove large temporary objects when no longer needed
* Consider `df.query()` or `df.loc[]` instead of large boolean masks
* For large datasets, process in chunks when possible

## Reproducibility Best Practices

* Add version information for key dependencies:
```python
import pandas as pd
import numpy as np
print(f"pandas: {pd.__version__}, numpy: {np.__version__}")
```

* Set random seeds in a dedicated, well-commented cell:
```python
# Set random seeds for reproducibility
import random
import numpy as np
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
```

* Save intermediate results for long-running notebooks:
```python
# Save checkpoint after expensive computation
processed_data.to_parquet("checkpoint_processed_data.parquet")
```

## Conclusion
