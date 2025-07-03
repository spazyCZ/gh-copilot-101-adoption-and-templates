# Custom GitHub Copilot Instructions Template

## Table of Contents

- [Introduction](#introduction)
- [Key Objectives](#key-objectives)
- [Core Guidelines](#core-guidelines)
  - [Documentation Standards](#1-documentation-standards)
  - [Type Safety](#2-type-safety)
  - [Testing Best Practices](#3-testing-best-practices)
  - [Logging Standards](#4-logging-standards)
  - [Additional Technical Requirements](#5-additional-technical-requirements)
- [Coding Style and Best Practices](#coding-style-and-best-practices)
- [Language-Specific Adaptations](#language-specific-adaptations)
- [Optional Application Patterns](#optional-application-patterns)

## Introduction

This document provides comprehensive guidelines for generating code using GitHub Copilot across different programming languages. The instructions combine universal best practices with project-specific requirements to ensure consistent, high-quality code generation.

## Key Objectives

✓ Generate clear, maintainable, and testing-friendly code
✓ Include thorough documentation and type declarations
✓ Create open-source quality code and documentation
✓ Ensure all new code components are well-documented
✓ Produce comprehensive tests for new functionality
✓ Follow language-specific best practices and conventions

## Core Guidelines

### 1. Documentation Standards

#### Required for all code

Every class, function, and method must have comments explaining their purpose:

**General Pattern:**

```javascript
// A class representing a data processor.
class DataProcessor {
    /**
     * Process data according to configured rules.
     * 
     * This class handles the transformation of input data
     * based on configuration parameters.
     */
    
    constructor(config) {
        /**
         * Initialize with configuration settings.
         * 
         * @param config - Dictionary/Object containing configuration parameters.
         */
        this.config = config;
    }
}
```

### 2. Type Safety

- Use the strongest type system available in your language
- Declare types for parameters, return values, and variables where supported
- Leverage language-specific type checking tools and conventions
- For dynamically typed languages, use type hints or annotations where available

**Examples by Language:**

- **TypeScript/JavaScript:** Use TypeScript interfaces and type annotations
- **Python:** Use type hints with `typing` module
- **Java/C#:** Use strong typing with generics
- **Go:** Use explicit type declarations
- **Rust:** Leverage the type system and ownership model

### 3. Testing Best Practices

- Write testable code by separating concerns and using dependency injection
- Create comprehensive test suites covering different scenarios and edge cases
- Use language-appropriate testing frameworks
- Split tests into unit tests, integration tests, and mock tests
- **Mark all AI-generated tests for manual review:**
  - Add appropriate markers or comments indicating AI generation
  - Include manual review reminders
- Follow the Arrange–Act–Assert pattern
- Use descriptive test names and include explanatory comments
- Set up clean test data and state

### 4. Logging Standards

- Use the primary logging mechanism for your language instead of basic print/console statements
- Configure appropriate log levels (DEBUG, INFO, WARN, ERROR)
- Include contextual information in log messages
- Follow structured logging practices where applicable

### 5. Additional Technical Requirements

#### Performance Optimization

- Write efficient algorithms with appropriate time complexity
- Minimize memory allocations and manage resources properly
- Use language-specific optimization techniques
- Profile critical code paths regularly
- Implement proper error handling and recovery mechanisms

#### Configuration Management

- Load configuration from environment variables or configuration files
- Never hardcode secrets or sensitive information
- Use appropriate configuration libraries for your language
- Implement secure configuration loading practices

## Coding Style and Best Practices

- **Modularity**: Write modular code that is easier to maintain and test
- **Consistency**: Follow language-specific naming conventions and coding standards
- **Error Handling**: Implement robust error and exception handling
- **Comments**: Document every class, method, and critical code section
- **Documentation**: Maintain up-to-date documentation for all public APIs
- **Readability**: Prioritize code clarity and maintainability
- **Idiomatic Code**: Write code that follows language-specific patterns and conventions

## Language-Specific Adaptations

### For Statically Typed Languages (Java, C#, TypeScript, etc.)

- Leverage compile-time type checking
- Use interfaces and abstract classes for better design
- Implement proper exception hierarchies
- Follow language-specific coding standards (e.g., C# naming conventions, Java best practices)

### For Dynamically Typed Languages (Python, JavaScript, Ruby, etc.)

- Use type hints/annotations where available
- Implement runtime type checking where necessary
- Follow language-specific style guides (PEP 8 for Python, etc.)
- Use linting tools to maintain code quality

### For Functional Languages (Haskell, F#, etc.)

- Embrace immutability and pure functions
- Use proper error handling mechanisms (Maybe, Either, etc.)
- Leverage pattern matching and algebraic data types
- Follow functional programming best practices

### For Systems Languages (Rust, C++, Go, etc.)

- Manage memory safely and efficiently
- Handle errors explicitly
- Use language-specific concurrency patterns
- Follow performance-oriented best practices

## Optional Application Patterns

### For Library/Module Development

- Provide clear public APIs with comprehensive documentation
- Include usage examples and integration guides
- Implement proper versioning and backward compatibility
- Create thorough test suites for public interfaces

### For Web Applications

- Separate business logic from presentation layers
- Implement proper security practices
- Use appropriate frameworks and follow their conventions
- Include API documentation and testing

### For CLI Applications

- Implement proper argument parsing
- Provide helpful usage information and error messages
- Use appropriate logging instead of direct output
- Include configuration file support where applicable

### For Microservices/Distributed Systems

- Implement proper service discovery and communication
- Use structured logging and monitoring
- Handle network failures gracefully
- Follow containerization best practices

## Conclusion

These instructions are designed to ensure that GitHub Copilot produces high-quality, maintainable code regardless of the programming language. Adapt these guidelines to your specific language and project requirements while maintaining the core principles of clarity, testability, and documentation.

**Note:** Remember to customize the language-specific sections based on your project's primary programming language(s) and remove sections that don't apply to your technology stack.
