# Copilot Adoption 101 — Playbooks & Instructions & Prompts  🚀🤖



 

> **TL;DR** — A “ready‑to‑eat” toolkit that shows you **how to adopt GitHub Copilot safely** in legacy projects *and* gives you **curated prompt recipes** per technology so you can start shipping value in minutes.

---
![Copilot Adoption 101 Banner](images/landing.png)


## 🍽️ Table of Contents

1. [Why this repo?](#why-this-repo)
2. [Folder layout](#folder-layout)
3. [Quick start ⚡](#quick-start-)
   * [Copilot Quick-Start for Beginners (20 mins)](adoption-playbooks/readme-copilot-101-in-20mins.md)
   * [Marking AI-Generated Tests for Manual Review](adoption-playbooks/readme-marking-tests-ai-generated.md)
4. [Ready‑to‑eat walkthrough](#ready-to-eat-walkthrough)
5. [Playbooks](#playbooks)
6. [Prompt library](#prompt-library)
7. [Contributing](#contributing)
8. [License](#license)

---

## Why this repo?

Legacy code + AI assistants can be a minefield: IP concerns, missing tests, weird build pipelines… This repo gives you:

* **Step‑by‑step playbooks** (`adoption-playbooks/`) for three project maturity levels.
* **Language‑specific samples** (`samples/`) with runnable code, per‑sample prompts, VS Code settings, and CI.
* **Custom Copilot instructions** to nudge the AI toward *your* style guide.
* **CI guard‑rails** that block unsafe Copilot suggestions (secrets, no tests, license issues).

Think of it as *“learn by cloning”* — fork it, tweak it, ship it.

---

## Folder layout

```text
.
├── adoption-playbooks/       # Level 1‑3 onboarding guides (Mermaid + markdown)
└── samples/                  # runnable tech demos
    ├── python-module/
    ├── python-web-flask/
    ├── java-springboot/
    └── typescript-general/
```

Each **sample** has its own **`.github/`** (prompt recipes, per‑sample CI) and **`.vscode/`** (extension list, launch configs) so you can open a folder and start coding immediately.

---

## Quick start ⚡

```bash
# 1 — Clone
$ git clone https://github.com/your-org/gh-copilot-101-adoption-and-samples.git
$ cd gh-copilot-101-adoption-and-samples

# 2 — Open a sample in VS Code (with Copilot enabled)
$ code samples/python-module

# 3 — Expermitent with Copilot
```

> **Tip:** The recommended extensions and settings pop up automatically thanks to the folder’s `.vscode/` files.

---

## Ready‑to‑eat walkthrough

Let’s improve `sum_numbers.py` in the **Python module** sample.

1. **Ask Copilot to understand the code**
   Open the file, trigger Copilot Chat and type:

   ```
   Explain this function and list three edge cases it might miss.
   ```
2. **Generate a test first**

   ```
   Write a pytest for sum_numbers() covering the edge cases you just identified.
   ```

   Commit the test **before** touching behaviour.
3. **Refactor safely**  (guard‑railed by coverage gate)

   ```
   Rewrite sum_numbers() to handle negative inputs and large lists efficiently.
   ```


That’s it — you’ve used Copilot to *understand*, *test*, and *improve* legacy code without breaking prod.

---

## Playbooks

Each project maturity level requires a slightly different adoption approach tailored to its code quality and documentation status.

| Project maturity level                             | Quick link                                                   | Diagram |
| ------------------------------------------- | ------------------------------------------------------------ | ------- |
| **Level 1** — Well‑tested, documented       | [`adoption-playbooks/level-1/`](adoption-playbooks/level-1/) |         |
| **Level 2** — No tests but decent structure | [`adoption-playbooks/level-2/`](adoption-playbooks/level-2/) |         |
| **Level 3** — Low quality, sparse docs      | [`adoption-playbooks/level-3/`](adoption-playbooks/level-3/) |         |

Each folder contains:

* **Checklist.md** — step‑by‑step tasks
* **`*.mmd`** — Mermaid source for the diagrams
* **Rendered images** you can drop into slides

---

## Prompt library

Prompt recipes live in **`samples/<tech>/.github/prompts/`** so they travel with the code they were tested on.
File naming convention:

```
<topic>[-agent_]context.prompt.md
```

Examples:

* `fix.prompt.md` — single‑shot fix instructions

* `improve-testability.prompt.md` — guidance for refactor‑for‑testability pattern

* `agent_fixing-tests.prompt.md` — multi‑turn agent to repair failing tests

Open any prompt file to copy‑paste into Copilot Chat *or* your favourite LLM playground.

---

## Expanded sample: `python-module/`

```text
samples/python-module/
├── .github/
│   ├── prompts/
│   │   ├── fix.prompt.md
│   │   ├── agent_fixing-tests.prompt.md
│   │   └── improve-testability.prompt.md
│   ├── copilot-instructions.md

├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── src/
│   ├── __init__.py
│   └── sum_numbers.py
├── tests/
│   └── test_sum_numbers.py
├── requirements.txt
└── README.md                # explains sample & how to run it
```

**Key files explained**

| File / folder                 | What it’s for                                                               |
| ----------------------------- | --------------------------------------------------------------------------- |
| `.github/prompts/*.prompt.md` | Task‑specific prompt recipes used in the walkthrough.                       |
| `copilot-instructions.md`     | Custom guidance that nudges Copilot toward PEP 8 + project patterns.        |
| `tests/`                      | Characterisation tests generated before modifying behaviour.                |
| `src/`                        | Code under test; start here when exploring the sample.                      |

---

## Contributing 🙌 – Contributors wanted!

We’re actively looking for maintainers, prompt engineers, test writers, and doc aficionados. Check the **help‑wanted** issues or start a Discussion if you have a new idea. Every small PR counts!

Found a better prompt? Have a killer workflow? We ❤️ PRs!

1. Fork & branch: `git switch -c feat/my‑awesome‑prompt`
2. Add your prompt file under the relevant sample’s `prompts/` folder.
3. Update that sample’s `README.md` with a short description.
4. Run `npm run lint && make test` to satisfy CI.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for coding standards and IP checklist.

---

## License

MIT — see [`LICENSE`](LICENSE).

> Logo and product names are trademarks of their respective owners. This repo is **not** affiliated with or endorsed by GitHub.
