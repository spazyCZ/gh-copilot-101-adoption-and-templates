# Instructions for Copilot to generate commit messages

## Commit Message Instructions

Keep commit messages short and concise.

Start your commit message with a **category emoji** from the list below to describe the purpose of the change.

Format: `<emoji>: <message>`

Examples:
✨ Add new search functionality
🐛 Fix crash when uploading files

### Categories

- 📊 **Data**: Updates or adds data.
  Example: `📊 Update population dataset`

- 🐛 **Bug**: Fixes a user-facing bug.
  Example: `🐛 Fix broken link in footer`

- 🔨 **Refactor**: Changes code without fixing bugs or adding features.
  Example: `🔨 Refactor chart rendering logic`

- ✨ **Enhance**: Improves existing functionality.
  Example: `✨ Improve chart loading speed`

- 🎉 **Feature**: Adds a new user-facing feature.
  Example: `🎉 Add dark mode support`

- 📜 **Docs**: Updates or adds documentation.
  Example: `📜 Add setup guide for developers`

- 🧹 **Chore**: Maintenance tasks like dependency updates.
  Example: `🧹 Update Node.js to latest version`

- 💄 **Style**: Formatting or linting changes.
  Example: `💄 Fix inconsistent indentation`

- 🚧 **WIP**: Work in progress for future commits.
  Example: `🚧 Add initial layout for dashboard`

- ✅ **Tests**: Adds or refactors tests.
  Example: `✅ Add missing unit tests`

---

### Tips
- Keep messages concise and clear.
- Use one emoji per commit for clarity.
- Split changes into separate commits if needed.

Original from: @Marigold [GitHub Copilot Commit Message Instructions](https://raw.githubusercontent.com/owid/etl/refs/heads/master/.copilot-commit-message-instructions.md)