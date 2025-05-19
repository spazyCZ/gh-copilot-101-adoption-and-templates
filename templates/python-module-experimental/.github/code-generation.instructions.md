---
applyTo: "**/*.{py,ipynb}"
---
# Code Generation Instructions

## General Principles
- Generate clear, maintainable, and testing-friendly code.
- Ensure all code includes thorough documentation and data type declarations.
- All new classes and methods must be well-documented with docstrings and comments.
- Use type hints for all function parameters and return values (Python).
- Use the primary logging mechanism for printing events (never use print directly).

## Asynchronous Programming
- Use async/await and non-blocking operations for asynchronous code.
- Implement proper exception handling in all async functions.
- Use async locks when modifying shared data structures (Python).
- Follow the existing pattern of using asyncio.create_task for non-blocking operations (Python).

## Performance Optimization
- Optimize for performance, especially in latency-sensitive environments.
- All code must be optimized for environments where microseconds matter.
- Implement efficient algorithms with O(1) or O(log n) time complexity where possible.

### Memory Management
- Minimize memory allocations and garbage collection triggers.
  - Use object pooling for frequently created/destroyed objects.
  - Pre-allocate buffers and arrays where sizes are predictable.

### Execution Path
- Avoid blocking operations in the main execution path.
  - Use non-blocking I/O operations.
  - Implement circuit breakers for external service calls.

### Data Structures
- Optimize data structures for quick access patterns.
  - Use fixed-size arrays instead of dynamic collections where appropriate.
  - Consider memory layout and cache locality for hot path data.

### Profiling and Benchmarking
- Profile and optimize critical code paths regularly.
  - Identify and eliminate bottlenecks.
  - Benchmark against defined latency SLAs.

### Dependencies
- Minimize external dependencies that could introduce latency.
- Use lock-free algorithms and data structures when possible.

## Environment Configuration
- All keys and environment variables must be read from a .env file. Use an appropriate library (e.g. python-dotenv for Python) to securely load these configurations.
- Do NOT hardcode any secrets; always load them from the .env file.
