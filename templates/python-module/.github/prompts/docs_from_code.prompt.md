---
mode: agent
---


# Produce Docs From Code – Copilot Prompt

Go thru the @codebase and generate comprehensive documentation files based on the source code structure, business logic, domain model, API specification, authentication/security mechanisms, and overall architecture.
---

## 0. Scan phase

1. **Parse** the repository's source code:

   * **Architecture Detection**: Determine if this is a microservice architecture, monolithic application, or hybrid approach.
   * **Service/Module Discovery**: 
     - For microservices: Detect service modules (top‑level folders, build files, service registries, package namespaces)
     - For monoliths: Identify application modules, blueprints, packages, and logical boundaries
   * **Route/Endpoint Analysis**: Identify HTTP/gRPC routes, Flask blueprints, controller/handler classes, and annotation‑based endpoints.
   * **Data Models**: Extract domain classes/structs, database models (SQLAlchemy, Django ORM, etc.), and their key fields and relationships.
   * **Business Logic**: Locate business‑logic clues in docstrings, comments, service layers, and complex `if/else`, `switch`, or rules‑engine constructs.
   * **Authentication & Authorization**: Identify authentication mechanisms, user roles, permission systems, and security patterns.
   * **Frontend Integration**: Analyze templates, static files, forms, API endpoints for AJAX, and client-server communication patterns.
   * **Configuration & Environment**: Examine configuration management, environment variables, and deployment settings.
   * **Testing Infrastructure**: Review test structure, test types (unit, integration, e2e), and test coverage patterns.
   * **User Journey Analysis**: Trace user interactions through templates, forms, routes, and business logic to identify complete user workflows.
2. **Ask** concise follow‑up questions if critical information is missing (e.g., unclear service boundaries, undocumented endpoints, or ambiguous authentication flows).

---

## 1. Output files

Return **EIGHT fenced blocks**, each starting with:

```text
FILE: docs/<file-name>
```

Generate these files:

| # | File name               | Purpose & internal heading                    |
| - | ----------------------- | --------------------------------------------- |
| 1 | `architecture.md`       | `## Application Architecture Overview`        |
| 2 | `business_logic.md`     | `## Business Logic & Functional Requirements` |
| 3 | `domain_model.md`       | `## Domain Data Model`                        |
| 4 | `database_structure.md` | `## Database Structure & Schema`              |
| 5 | `api_spec.yaml`         | Complete OpenAPI 3.1 spec in YAML             |
| 6 | `auth_security.md`      | `## Authentication & Security`                |
| 7 | `user_flow_diagrams.md` | `## User Flow Diagrams`                       |
| 8 | `README.md`             | Doc hub with links & diagram index            |

---

### **architecture.md**

* **Application Type**: Clearly state if this is microservices, monolith, or hybrid.
* **Module/Service catalog** list: `<ModuleName>: one‑sentence purpose`.
* **Context diagram**: 
  - For microservices: Mermaid `flowchart` showing services + comms
  - For monoliths: Show major modules/blueprints and their interactions
* **Technology Stack**: Framework, database, frontend tech, deployment approach.
* **Directory Structure**: Key folders and their purposes.

### **business\_logic.md**

For every inferred use‑case:

1. **Title** (verb phrase)
2. **Actors** (roles, user types, external systems)
3. **Step‑by‑step flow** (numbered)
4. **Business rules** (bullets)
5. **Validation rules** (input validation, authorization checks)
6. Optional `stateDiagram‑v2` for entity lifecycles.
   *Ask if particulars are ambiguous.*

### **domain\_model.md**

* **Entity table**: `Entity | Description | Key attributes (name:type:constraints)`.
* **Relationships**: Describe how entities relate to each other.
* **Mermaid erDiagram** expressing relationships.
* **Database Schema**: Table structures, indexes, constraints.
* **Data Access Patterns**: How data flows through the application.
* State data retention/compliance constraints if applicable.

### **database\_structure.md**

* **Database Type**: Specify the database system (PostgreSQL, MySQL, SQLite, etc.) and version.
* **Connection Configuration**: How the application connects to the database (connection strings, pools, etc.).
* **Table Structure**: For each table, document:
  - Table name and purpose
  - Column definitions with data types, constraints, and descriptions
  - Primary keys and foreign key relationships
  - Indexes and their purposes
  - Triggers or stored procedures (if any)
* **Mermaid ERD**: Create a comprehensive `erDiagram` showing:
  - All tables and their relationships
  - Cardinality (one-to-one, one-to-many, many-to-many)
  - Key constraints and foreign key relationships
* **Migration Strategy**: How database schema changes are managed
* **Data Seeding**: Initial data requirements and seed scripts
* **Performance Considerations**: Indexing strategy, query optimization notes
* **Database Constraints & Rules**: Business rules enforced at the database level

### **api\_spec.yaml**

* Full OpenAPI 3.1 contract derived from route signatures.
* Paths, methods, parameters, schemas (reuse entities via `$ref`).
* **Authentication**: Document auth mechanisms (JWT, session, API keys).
* **Error Responses**: Standard error format with examples.
* **Request/Response Examples**: Include one worked example per main endpoint.
* **Rate Limiting**: If applicable, document throttling rules.

### **auth\_security.md**

* **Authentication Methods**: How users authenticate (login forms, tokens, etc.).
* **Authorization Model**: User roles, permissions, access control patterns.
* **Security Measures**: CSRF protection, input validation, secure headers.
* **Session Management**: How sessions are handled, timeout policies.
* **Password Policy**: Requirements, hashing, reset procedures.
* **Security Configuration**: Environment variables, secrets management.

### **user\_flow\_diagrams.md**

* **Mapping Table**: User flows mapped to Flask views/blueprints and templates with clickable links.
* **User Journey Flows**: For each major user journey, create Mermaid `flowchart TD` diagrams showing:
  - User actions and system responses
  - Template files used at each step (with href links to actual files)
  - Form submissions and validations
  - Success/error paths
  - Blueprint endpoints involved
* **Advanced Formatting**: Use HTML entities, emojis, and styling in Mermaid diagrams for visual appeal:
  - Strong tags for emphasis: `<strong>Step Title</strong>`
  - Emojis for visual cues: 🚀 START, ✅ Success, ❌ Error, 📄 Template, 🔗 Endpoint
  - Href links to template files: `<a href='../path/to/template.html'><em>template.html</em></a>`
* **Key User Flows** to document:
  - User registration and login
  - Main feature workflows (based on business logic)
  - Admin/management flows
  - Error handling paths

### **README.md** (System Documentation Hub)

* **About**: Brief description of the application's purpose and main features.
* **Quick Start**: Brief setup and run instructions.
* **Documentation Links**: Bullet links to the seven sibling docs.
* **## Diagram Index (Mermaid)**: list each diagram produced, e.g.
  `- Architecture: flowchart (system-overview)`
  `- User flow: flowchart TD (user-journeys)`
  `- Domain model: erDiagram (entities-relationships)`
  `- Database structure: erDiagram (database-schema)`
* **Key Features**: Main functionality highlights.
* **Configuration**: Important environment variables and settings.
* **Change Log**: Chronological list of major changes and releases. (version, date, jira id, description)

---

## 2. Formatting rules

* Use GitHub‑flavored Markdown inside all `.md` files.
* Every diagram or YAML spec must be fenced with proper syntax highlighting.
* Keep prose concise; no implementation code snippets.
* If you cannot find enough code evidence for a section, ask before generating it.
* For Flask applications, pay special attention to:
  - Blueprint organization and route structure
  - SQLAlchemy models and relationships
  - Form classes and validation rules
  - Template inheritance and static file organization
  - Service layer patterns and business logic separation
  - User flow patterns from templates through routes to business logic
  - Database model definitions and migration files
* For database documentation:
  - Parse SQLAlchemy model classes for table definitions
  - Identify relationships between models (ForeignKey, relationship())
  - Document database constraints and indexes
  - Include migration files analysis for schema evolution
  - Map ORM models to actual database tables
* For authentication systems, document:
  - User model and role definitions
  - Login/logout flows
  - Permission checking mechanisms
  - Session management approach
* For user flow diagrams:
  - Trace complete user journeys from UI to backend
  - Include both happy path and error scenarios
  - Map each step to specific template files and routes
  - Use consistent visual formatting with HTML entities and emojis
* End the chat response after the last `FILE:` block – no extra commentary.
* If you cannot generate any files, explain why in the chat.
* If you cannot generate part of the files, explain which parts are missing and why.