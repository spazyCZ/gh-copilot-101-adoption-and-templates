# Copilot Review Instructions

This document outlines the guidelines and best practices for reviewing code generated by GitHub Copilot in this project. Adhering to these instructions ensures that the generated code meets the project's quality, performance, and maintainability standards.

## Objectives
- Ensure the generated code is clear, maintainable, and testing-friendly.
- Verify that the code adheres to the project's coding standards and guidelines.
- Confirm that the code includes proper documentation, type declarations, and logging.
- Validate that the code is optimized for performance and adheres to the project's tech stack.

---

## Review Checklist

### 1. Documentation and Comments
- [ ] Does every class and method include comments explaining their purpose and functionality?
- [ ] Are docstrings provided for all functions, including parameter and return type descriptions?
- [ ] Are comments clear, concise, and relevant?

### 2. Data Type Declarations
- [ ] Are data types declared for all function parameters and return values?
- [ ] Are type hints consistent with the project's requirements?

### 3. Testing
- [ ] Are unit tests provided for all new classes and methods?
- [ ] Do the tests cover edge cases and different scenarios?
- [ ] Are mocked tests named using the `test_mocked_*` convention?
- [ ] Are unit tests named using the `test_unit_*` convention?
- [ ] Are integration tests named using the `test_integration_*` convention?
- [ ] Are end-to-end tests named using the `test_e2e_*` convention?
- [ ] Are test files and classes named consistently (e.g., `test_module_name.py` and `TestModuleName`)?
- [ ] Are tests placed in the designated test directories?

### 4. Logging
- [ ] Is the primary logging mechanism used instead of print statements?
- [ ] Are log messages clear and informative?
- [ ] Are appropriate log levels (e.g., INFO, ERROR) used?

### 5. Asynchronous Programming
- [ ] Are async/await patterns used consistently in asynchronous code?
- [ ] Is proper exception handling implemented in async functions?
- [ ] Are async locks used when modifying shared data structures?
- [ ] Are non-blocking operations implemented using `asyncio.create_task` where applicable?

### 6. Performance Optimization
- [ ] Is the code optimized for low-latency environments (e.g., high-frequency trading)?
  - Example: Ensure critical operations complete within 1 millisecond (1000 microseconds) or less for high-frequency trading scenarios.
- [ ] Are efficient algorithms with O(1) or O(log n) complexity used where possible?
- [ ] Are memory allocations minimized, and object pooling used for frequently created/destroyed objects?
- [ ] Are blocking operations avoided in the main execution path?
- [ ] Are data structures optimized for quick access patterns?
- [ ] Are critical code paths profiled and benchmarked against latency SLAs?

### 7. Coding Style and Best Practices
- [ ] Is the code modular and easy to maintain?
- [ ] Are naming conventions and coding standards followed consistently?
- [ ] Is robust error and exception handling implemented?
- [ ] Are comments provided for critical sections of the code?

### 8. Tech Stack Compliance
- [ ] Does the code align with the project's default tech stack (e.g., Python, asyncio, unittest, pytest)?
- [ ] Are new dependencies added to `requirements.txt` if applicable?

---

## Additional Notes
- If any issues are identified during the review, provide clear and actionable feedback by specifying the problem, suggesting a solution, and including examples or links to relevant documentation where applicable.
- Ensure that the code adheres to the project's evolving requirements and guidelines.
- Collaborate with the team to iterate on these instructions as needed.

By following this checklist, we can maintain a high standard of quality and consistency in the codebase.
