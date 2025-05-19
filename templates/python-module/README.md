# Python Module Template

This directory contains example Python CLI applications for summing numbers.

## Directory Structure

```
python-module/
├── src/
│   ├── sum_numbers-instructed.py
│   └── sum_numbers-without-instructions.py
└── .github/
    └── prompts/
        ├── agent_fixing-tests.prompt.md
        ├── fix.prompt.md
        ├── improve-testability.prompt.md
    ├── copilot-instructions.md
    └── copilot-review-instructions.md
```

- `sum_numbers-instructed.py`: CLI app with inline comments and step-by-step instructions.
- `sum_numbers-without-instructions.py`: Minimal CLI app without comments or instructions.

> **Why are instructions important?**  
> As seen in the difference between the two files, instructions and comments help make code more understandable, maintainable, and easier for others to extend or debug.

## About the `.github` Directory

If present, the `.github` directory contains community health files such as issue templates, pull request templates, and contributing guidelines.  
These files help standardize collaboration and communication for this project.

### `.github/prompts`

This subdirectory contains prompt templates and instructions for GitHub Copilot and related automation:

- `agent_fixing-tests.prompt.md`: Prompt for an agent to fix failing tests.
- `fix.prompt.md`: Prompt template for general code fixes.
- `improve-testability.prompt.md`: Prompt for improving code testability.
- `copilot-instructions.md`: Instructions for Copilot's behavior and code suggestions.
- `copilot-review-instructions.md`: Instructions for Copilot to review code or pull requests.

These files are used to guide Copilot or other automation tools in generating, fixing, or reviewing code according to project standards.
