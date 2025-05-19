# Agent Test Fix Prompt

## Objective
Guide the agent to execute tests, fix issues, and ensure all tests pass while following project standards.

## Instructions

1. **Run Tests**:
   - Execute the test suite (e.g., `pytest`).
   - Capture all output, including errors and failures.

2. **Analyze Errors**:
   - Review test output to identify root causes.
   - Locate and note problematic code sections.

3. **Apply Fixes**:
   - Correct code to resolve issues.
   - Ensure all changes:
     - Include documentation and comments.
     - Declare data types for all methods/functions.
     - Separate business logic from views.
     - Use dependency injection where possible.

4. **Re-run Tests**:
   - Re-execute the test suite to confirm fixes.
   - Repeat until all tests pass.

5. **Logging and Reporting**:
   - Use the primary logging system for significant events.
   - Summarize changes and final test results.


## Example Workflow

Repeate flow until all tests pass

1. **Run Tests**:
   ```bash
   pytest > test_output.log
   ```

2. **Analyze Failures**:
   - Review `test_output.log` for errors.

3. **Apply Fixes**:
   - Edit relevant files to resolve issues.

4. **Re-run Tests**:
   ```bash
   pytest
   ```

5. **Log and Report**:
   - Log changes and results using the primary logger.
   - Summarize fixes and outcomes.

## Notes
- Test and document all changes.
- Follow project coding standards.
- Write modular, maintainable code for future updates and testing.
