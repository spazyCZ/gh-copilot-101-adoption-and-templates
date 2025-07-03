# Instructions for Copilot to generate pull request descriptions

When creating pull request descriptions, follow these guidelines to ensure consistency and clarity:

## Title Format
- Use imperative mood (e.g., "Fix bug in authentication" not "Fixed bug in authentication")
- Keep it concise (50 characters or less)
- Start with a verb (Add, Fix, Update, Remove, Refactor, etc.)
- Capitalize the first letter

## Description Structure

### Summary
- Provide a brief overview of what this PR accomplishes
- Explain the problem being solved or feature being added
- Keep it clear and concise

### Changes Made
List the key changes in bullet points:
- **Added:** New features, files, or functionality
- **Modified:** Changes to existing code or behavior
- **Fixed:** Bug fixes and issue resolutions
- **Removed:** Deleted files, features, or deprecated code
- **Refactored:** Code improvements without changing functionality

### Testing
- Describe how the changes were tested
- Include any new test cases added
- Mention if manual testing was performed
- Note any edge cases considered

### Breaking Changes
- Clearly highlight any breaking changes
- Explain the impact on existing functionality
- Provide migration instructions if applicable

### Additional Notes
- Link to related issues using keywords (Fixes #123, Closes #456)
- Mention any dependencies or prerequisites
- Include screenshots for UI changes
- Add performance impact notes if relevant

## Code Quality Checklist
Before submitting, ensure:
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated if needed
- [ ] No sensitive information is exposed
- [ ] Error handling is appropriate
- [ ] Performance impact is acceptable

## Review Guidelines
- Tag appropriate reviewers
- Use draft PR for work in progress
- Respond to feedback promptly
- Keep PR scope focused and manageable

## Examples

### Good Title Examples:
- "Add user authentication middleware"
- "Fix memory leak in data processing"
- "Update dependencies to latest versions"
- "Refactor database connection logic"

### Good Description Example:
```
## Summary
Implements user authentication middleware to secure API endpoints.

## Changes Made
- **Added:** JWT-based authentication middleware
- **Added:** User login/logout endpoints
- **Modified:** Protected routes to require authentication
- **Added:** Unit tests for authentication flow

## Testing
- Added 15 new unit tests covering authentication scenarios
- Manual testing performed on all protected endpoints
- Tested with valid and invalid JWT tokens

## Breaking Changes
None - this is additive functionality only.

## Additional Notes
Closes #42
Requires environment variable JWT_SECRET to be set
```

## Template
Use this template as a starting point:

```markdown
## Summary
[Brief description of what this PR does]

## Changes Made
- **Added:** 
- **Modified:** 
- **Fixed:** 
- **Removed:** 

## Testing
[Describe testing approach and results]

## Breaking Changes
[List any breaking changes or write "None"]

## Additional Notes
[Any additional context, links to issues, etc.]
```