# GitHub Copilot Prompt: Improve Testability and Debugging

When generating code, always prioritize the following:

1. **Testability**
   - Write code that is modular and easy to test.
   - Separate business logic from UI, database, and external dependencies.
   - Use dependency injection where possible.
   - Ensure all public methods and APIs have corresponding unit tests.
   - Facilitate mocking of external services and dependencies in tests.
   - Place tests in dedicated files, using clear and consistent naming conventions.

2. **Debugging**
   - Integrate robust error handling and meaningful exception messages.
   - Use the primary logging mechanism (e.g., Python's `logging` module) for all event and error reporting.
   - Avoid using print statements for debugging; prefer structured logging.
   - Add comments to clarify complex logic and potential failure points.
   - Ensure logs include context (such as function names, parameters, and error details) to aid in troubleshooting.

3. **Documentation**
   - Document all classes, methods, and functions with docstrings explaining their purpose, parameters, and return values.
   - Include comments for any non-obvious implementation details or debugging tips.

4. **General**
   - Adhere to project coding standards and best practices.
   - Use type annotations for all function signatures.

By following these guidelines, generated code will be easier to test, debug, and maintain.
