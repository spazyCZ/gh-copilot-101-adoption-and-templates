# Agent Run Test and Optimize Code Prompt for Spring Boot

## Objective
This prompt is designed to guide the agent in executing tests, identifying performance bottlenecks, and optimizing the code for a Spring Boot application to improve performance while ensuring all tests pass successfully.

## Instructions

1. **Test Execution**:
   - Execute the test suite using the appropriate test runner (e.g., `mvn test` or `gradle test`).
   - Capture the output of the test execution, including any errors or failures.

2. **Error and Performance Analysis**:
   - Analyze the test output to identify the root cause of any failures.
   - Use profiling tools (e.g., `VisualVM`, `JProfiler`, or `YourKit`) to identify performance bottlenecks in the code.
   - Locate the relevant code files and lines causing the issues or inefficiencies.

3. **Fix Implementation**:
   - Apply fixes to the code to resolve the identified issues and optimize performance.
   - Ensure that the fixes adhere to the project's coding guidelines, including:
     - Proper documentation and comments using Javadoc.
     - Use of dependency injection and Spring's best practices.
     - Separation of concerns (e.g., controllers, services, repositories).
   - Optimize database queries, loops, and other computationally expensive operations.

4. **Re-run Tests**:
   - After applying fixes, re-run the test suite to verify that the issues have been resolved and performance has improved.
   - Repeat the process until all tests pass successfully and performance is optimized.

5. **Logging and Reporting**:
   - Use the primary logging mechanism (e.g., SLF4J with Logback) to log significant events during the process.
   - Provide a summary of the changes made, performance improvements, and final test results.

## Example Workflow

1. **Run Tests**:
   ```bash
   mvn test > test_output.log
   ```

2. **Analyze Failures and Performance**:
   - Review `test_output.log` to identify failing tests and error messages.
   - Use profiling tools to identify performance bottlenecks.

3. **Apply Fixes and Optimizations**:
   - Edit the relevant code files to address the issues and optimize performance.

4. **Re-run Tests**:
   ```bash
   mvn test
   ```

5. **Log and Report**:
   - Log the changes, performance improvements, and results using the primary logging mechanism.
   - Provide a summary of the fixes, optimizations, and test outcomes.

## Notes
- Ensure that all changes are thoroughly tested and documented.
- Follow the project's coding standards and best practices.
- Use modular and maintainable code to facilitate future updates and testing.
- Prioritize optimizations that have the most significant impact on performance.
- Ensure proper use of Spring Boot features like caching, asynchronous processing, and database connection pooling for performance improvements.
