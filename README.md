# Copilot Adoption 101 — (instructions + prompts) & adoption playbooks  🚀🤖

 

> **TL;DR** — A “ready‑to‑eat” toolkit that shows you **how to adopt GitHub Copilot safely** in legacy projects *and* gives you **curated prompt recipes** per technology so you can start shipping value in minutes.  
>  
> 👉 **[Browse the templates](templates/)** — including the <span style="background: #ffe066; padding: 0 4px; border-radius: 3px;">🆕 new</span> **[Jupyter](templates/jupyter)** template and our most crafted **[python-module](templates/python-module/)** sample 🚀 ✨.

--- 
![Copilot Adoption 101 Banner](images/landing.png)

## 🍽️ Table of Contents

1. [Why this repo?](#why-this-repo)
2. [Main folders](#main-folders)
3. [Quick start ⚡](#quick-start-)
   * [Copilot Quick-Start for Beginners (20 mins)](adoption-playbooks/readme-copilot-101-in-20mins.md)
   * [Marking AI-Generated Tests for Manual Review](adoption-playbooks/readme-marking-tests-ai-generated.md)
4. [🚀 Explore the Templates](#-explore-the-templates)
5. [🎯 Playbooks](#playbooks)
6. [Contributing](#contributing)
7. [License](#license)

---

## Why this repo?

Legacy code + AI assistants can be a minefield: IP concerns, missing tests, weird build pipelines… This repo gives you:

* **Step‑by‑step playbooks** (`adoption-playbooks/` //TODO) for three project maturity levels.
* **Language‑specific templates** (`templates/` [link](templates/README.md) ) with runnable code, per‑template prompts, VS Code settings, and CI.
* **Custom Copilot instructions** to nudge the AI toward *your* style guide.
* **Prompt recipes** for common tasks, so you can *“learn by doing”*

Think of it as *“learn by cloning”* — fork it, tweak it, ship it.

---

## Main folders

```text
.
├── adoption-playbooks/       # Level 1‑3 onboarding guides (Mermaid + markdown)
└── templates/                # templates for different languages
    
```

Each **template** has its own **`.github/`** (prompt recipes, per‑template CI) and **`.vscode/`** (extension list, launch configs) so you can open a folder and start coding immediately.


---


## Quick start ⚡

```bash
# 1 — Clone
$ git clone https://github.com/your-org/gh-copilot-101-adoption-and-samples.git
$ cd gh-copilot-101-adoption-and-samples

# 2 — Open a sample in VS Code (with Copilot enabled)
$ code templates/python-module

# 3 — Experiment with Copilot
```

> **Tip:** The recommended extensions and settings pop up automatically thanks to the folder’s `.vscode/` files.

---


## 🚀 Explore the Templates

Curious how Copilot works in real projects? Jump into the [templates/](templates/README.md) folder to try runnable demos organized by technology (e.g., Python, Java, TypeScript, etc.). Each template includes ready-to-run code, prompt recipes, and custom Copilot instructions—perfect for hands-on learning!


### Expanded sample: `templates/python-module/`

```text
templates/python-module/
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


--

## Playbooks

Each project maturity level requires a slightly different adoption approach tailored to its code quality and documentation status.

| Project maturity level                             | Quick link                                                   | Status |
| ------------------------------------------- | ------------------------------------------------------------ | ------- |
| **Level 1** — Well‑tested, documented       | [`adoption-playbooks/level-1/`](adoption-playbooks/README.md) |  🔴 not started          |
| **Level 2** — No tests but decent structure | [`adoption-playbooks/level-2/`](adoption-playbooks/README.md) | 🔴 not started           |
| **Level 3** — Low quality, sparse docs      | [`adoption-playbooks/level-3/`](adoption-playbooks/README.md) |   🔴 not started         |

Each folder *will* contain:

* **Checklist.md** — step‑by‑step tasks
* **`*.mmd`** — Mermaid source for the diagrams
* **Rendered images** you can drop into slides

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
