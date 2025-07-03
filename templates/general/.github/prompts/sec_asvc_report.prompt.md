---
mode: agent
---
# GitHub Copilot Custom Prompt for OWASP ASVS 5.0.0 JSON

This file customizes the context Copilot uses to generate code and suggestions when working with the OWASP Application Security Verification Standard 5.0.0 in CycloneDX JSON format.

---

## Instructions for Copilot

You are working with the OWASP Application Security Verification Standard (ASVS) version 5.0.0, provided as a CycloneDX JSON Software Bill of Materials (SBOM) located at:

- `5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.cdx.json`
- [GitHub Source](https://raw.githubusercontent.com/OWASP/ASVS/refs/heads/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.cdx.json)

### File Structure

- The file is in [CycloneDX JSON format](https://cyclonedx.org/docs/1.6/json/), version 1.6.
- Security requirements are located under:
  - `declarations.standards[0].requirements`
- Each requirement typically has:
  - `identifier` (e.g., "V1.1.1"),
  - `title` (may be present; e.g., "Encoding and Sanitization Architecture"),
  - `text` (may be present; e.g., "Verify that input is decoded..."),
  - `parent` (references the parent requirement/category).


### Status Tracking

For each requirement, track fulfillment status using these values:
- ✅ **Compliant**: Requirement is fully implemented and verified
- ⚠️ **Partial**: Requirement is partially implemented or needs improvement
- ❌ **Non-Compliant**: Requirement is not implemented
- ⏳ **In Progress**: Requirement is currently being implemented
- 📋 **Not Applicable**: Requirement doesn't apply to this project
- 🔍 **Needs Review**: Implementation status requires further investigation

### Example Output (Markdown Table with Status)

| Identifier | Title                          | Requirement Text                                     | Status | Implementation Notes | Evidence/Location |
|------------|-------------------------------|------------------------------------------------------|--------|---------------------|-------------------|
| V1.1.1     | Encoding and Sanitization Arch| Verify that input is decoded or unescaped ...        | ✅     | Flask-WTF validates all forms | `forms.py:15-30` |
| V1.2.4     | Injection Prevention          | Verify that data selection or database queries ...    | ⚠️     | SQLAlchemy ORM used, but raw SQL in reports | `models.py`, `reports.py:45` |
| V2.1.1     | Password Security             | Verify that user passwords are at least 12 chars... | ❌     | Current min length is 8 chars | `auth/validators.py:22` |
| V3.2.1     | Session Management            | Verify that session tokens are generated...          | ⏳     | Implementing secure session handling | PR #123 |


### Output Format table Non-Compliant
 *** create separate table Non-Compliant requirements and sort them by criticality

---

## tasks

### 0. Scan phase

1. **Parse** the JSON file:
   - Identify the structure and key fields.
   - Extract all requirements from `declarations.standards[0].requirements`.

2. **Organize** the requirements:
    - Make list of all requirements that are valid for that project #codespace
3. **Analysis**:
   - Analyze the code that requirement is fulfilled
   - Identify any missing requirements or gaps in coverage.
   - Assign status to each applicable requirement
   - Document evidence of compliance or non-compliance

### 2. Output phase

Generate a comprehensive security compliance report including:

1. **Executive Summary**:
   - Overall compliance percentage
   - Critical gaps requiring immediate attention
   - Compliance status breakdown by category

2. **Detailed Requirements Table**:
   - All applicable requirements with status tracking
   - Implementation notes and evidence references
   - Remediation recommendations for non-compliant items

3. **Risk Assessment**:
   - High-priority security gaps
   - Recommended implementation timeline
   - Resource requirements for compliance

4. **Compliance Checklist**:
   - Organized by ASVS categories (V1, V2, V3, etc.)
   - Hierarchical structure using parent relationships
   - Actionable items for each requirement

**RESULT STORE TO FILE: `docs/asvs_compliance_report.md`**

---

