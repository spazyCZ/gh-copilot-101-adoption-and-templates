---
mode: agent
---

# Documentation Alignment Report – Copilot Prompt

Analyze the existing documentation in the `docs/` folder and compare it against the expected documentation structure defined in the `docs_from_code.prompt.md` file. Generate a comprehensive alignment report that identifies gaps, inconsistencies, and recommendations for improvement.

---

## 0. Analysis Phase

1. **Scan Existing Documentation**:
   - List all files currently in the `docs/` folder
   - Analyze the content structure and completeness of each file
   - Identify the documentation format and style used
   - Check for broken links or missing references

2. **Compare Against Expected Structure**:
   - Reference the 8 required documentation files from `docs_from_code.prompt.md`:
     1. `architecture.md`
     2. `business_logic.md`
     3. `domain_model.md`
     4. `database_structure.md`
     5. `api_spec.yaml`
     6. `auth_security.md`
     7. `user_flow_diagrams.md`
     8. `README.md`

3. **Content Quality Assessment**:
   - Evaluate if existing content matches the expected sections and depth
   - Check for required Mermaid diagrams and their completeness
   - Verify API specification completeness and format
   - Assess documentation consistency and accuracy

---

## 1. Report Structure

Generate a comprehensive report with the following sections:

### **Executive Summary**
- Overall documentation completeness percentage
- Key findings and critical gaps
- Priority recommendations for improvement

### **File-by-File Analysis**

For each of the 8 expected documentation files, provide:

#### **[File Name] - Status: [✅ Complete | ⚠️ Partial | ❌ Missing | 🔄 Needs Update]**

**Expected Content (from docs_from_code.prompt.md):**
- List the required sections and elements

**Current Status:**
- File existence: [Yes/No]
- Content completeness: [Percentage or description]
- Required sections present: [List with ✅/❌ status]
- Mermaid diagrams present: [List with ✅/❌ status]

**Gap Analysis:**
- Missing sections or content
- Incomplete or outdated information
- Format inconsistencies

**Recommendations:**
- Specific actions needed to align with expectations
- Priority level: [High/Medium/Low]

### **Cross-Reference Analysis**

**Internal Documentation Links:**
- Check if README.md properly links to all other documentation files
- Verify diagram index completeness and accuracy
- Identify broken internal references

**Code-Documentation Alignment:**
- Compare documented API endpoints with actual route implementations
- Verify model documentation matches actual database models
- Check if business logic documentation reflects current code implementation

### **Quality Assessment**

**Format Consistency:**
- Markdown formatting standards adherence
- Mermaid diagram syntax and style consistency
- YAML specification format compliance

**Content Accuracy:**
- Documentation reflects current codebase state
- Version alignment between docs and code
- Configuration and setup instructions accuracy

**Completeness Metrics:**
- Documentation coverage percentage by category
- Missing critical information areas
- User journey documentation completeness

### **Compliance Matrix**

Create a table showing alignment with `docs_from_code.prompt.md` requirements:

| Requirement Category | Expected | Current Status | Compliance % | Priority |
|---------------------|----------|----------------|--------------|----------|
| Architecture Overview | ✅ | [Status] | [%] | [Level] |
| Business Logic | ✅ | [Status] | [%] | [Level] |
| Domain Model | ✅ | [Status] | [%] | [Level] |
| Database Structure | ✅ | [Status] | [%] | [Level] |
| API Specification | ✅ | [Status] | [%] | [Level] |
| Auth & Security | ✅ | [Status] | [%] | [Level] |
| User Flow Diagrams | ✅ | [Status] | [%] | [Level] |
| Documentation Hub | ✅ | [Status] | [%] | [Level] |

### **Action Plan**

**Immediate Actions (High Priority):**
- List critical gaps that need immediate attention
- Missing files that should be created first
- Broken links or references that need fixing

**Short-term Improvements (Medium Priority):**
- Content updates and expansions needed
- Diagram additions or improvements
- Format standardization tasks

**Long-term Enhancements (Low Priority):**
- Advanced documentation features
- Additional diagrams or visualizations
- Documentation automation opportunities

### **Templates and Examples**

**Missing File Templates:**
- Provide basic templates for any missing documentation files
- Include required sections and formatting examples

**Improvement Examples:**
- Show before/after examples for incomplete sections
- Provide sample Mermaid diagrams that are missing
- Give examples of proper cross-referencing

---

## 2. Formatting Guidelines

**Report Format:**
- Use clear markdown formatting with proper headers
- Include emoji indicators for status (✅ ⚠️ ❌ 🔄)
- Use tables for structured comparisons
- Provide actionable recommendations with specific steps

**Status Indicators:**
- ✅ **Complete**: Fully aligned with expectations
- ⚠️ **Partial**: Present but incomplete or needs improvement
- ❌ **Missing**: File or section not present
- 🔄 **Needs Update**: Present but outdated or inaccurate

**Priority Levels:**
- 🔴 **High**: Critical gaps affecting usability
- 🟡 **Medium**: Important improvements for completeness
- 🟢 **Low**: Nice-to-have enhancements

---

## 3. Analysis Instructions

1. **Read all existing documentation files** in the `docs/` folder
2. **Compare against the detailed requirements** in `docs_from_code.prompt.md`
3. **Analyze the current codebase** to verify documentation accuracy
4. **Generate specific, actionable recommendations** for each gap or inconsistency
5. **Prioritize improvements** based on impact on user experience and documentation completeness
6. **Provide templates or examples** for missing or incomplete sections

**Focus Areas:**
- Documentation completeness vs. expected structure
- Content accuracy vs. current codebase implementation
- Format consistency and professional presentation
- User experience and navigation between documentation files
- Technical accuracy of diagrams, API specs, and code examples

---

## 4. Deliverable

Generate a single comprehensive report that can be used to:
- Understand current documentation status
- Plan documentation improvement efforts
- Track progress against the expected documentation standard
- Ensure alignment between code and documentation

The report should be actionable, specific, and provide clear guidance for bringing the documentation up to the standards defined in `docs_from_code.prompt.md`.
