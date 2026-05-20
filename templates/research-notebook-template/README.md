# Research Notebook Template

A Git-friendly template for computational research with Jupyter notebooks. Pre-configured with tools that make notebooks and Git play nicely together.

## ✨ What This Does

- **`nbstripout` pre-configured** — notebook outputs are automatically stripped before every commit. No more 50MB diffs from cell outputs.
- **`jupytext` ready** — sync notebooks with plain `.py` files for readable diffs and code review.
- **GitHub Action** — validates that all notebooks execute without errors on every push.
- **Devcontainer** — open in Codespaces or VS Code for an instant, reproducible environment.
- **Clean separation** — notebooks for exploration, `src/` for reusable code.

## 📁 Structure

```
├── notebooks/              ← Jupyter notebooks (exploration, analysis)
│   └── 01_exploration.ipynb
├── src/                    ← Reusable Python modules
│   └── data.py             ← Data loading and cleaning functions
├── data/                   ← Data files (not tracked by Git)
├── outputs/                ← Generated figures and results (not tracked)
├── requirements.txt        ← Python dependencies
├── jupytext.toml           ← Jupytext configuration
├── .devcontainer/          ← Codespaces / VS Code dev environment
└── .github/workflows/
    └── validate-notebooks.yml  ← CI: runs all notebooks on push
```

## 🚀 Getting Started

### Option 1: GitHub Codespaces (no setup)
1. Click **Code → Codespaces → New codespace**
2. Wait for the environment to build (~2 min first time)
3. Open any notebook and start working
4. `nbstripout` is already active — just commit normally

### Option 2: Local Setup
```bash
# Clone and set up
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Install the nbstripout Git filter
nbstripout --install
```

## 📓 How Notebooks Stay Git-Friendly

### The Problem
Jupyter notebooks are JSON files. Cell outputs (tables, plots, errors) bloat diffs, make code review impossible, and inflate repo size.

### The Solution: `nbstripout`
This template installs `nbstripout` as a **Git filter**. When you `git add` a notebook, outputs are automatically stripped from the committed version. Your local notebook keeps its outputs — only the Git version is clean.

```bash
# Verify it's active
nbstripout --status
```

### Bonus: `jupytext`
For even cleaner diffs, `jupytext` syncs each notebook with a plain `.py` file:

```bash
# Pair a notebook with a .py file
jupytext --set-formats notebooks///ipynb,src///py:percent notebooks/01_exploration.ipynb

# The .py version has clean, reviewable diffs
git diff src/01_exploration.py
```

## 🧪 Continuous Integration

Every push runs the GitHub Action which:
1. Installs dependencies
2. **Executes every notebook** from top to bottom — catches broken imports, stale references, and errors
3. Runs `pytest` on `src/` (if tests exist)
4. Lints with `ruff`

If a notebook can't execute cleanly, the CI fails. This ensures your analysis is always reproducible.

## 📐 Project Conventions

| Guideline | Why |
|-----------|-----|
| **Notebooks for exploration, `src/` for functions** | Reusable code belongs in importable modules, not hidden in cell 47 |
| **Number your notebooks** (`01_`, `02_`, ...) | Makes the analysis sequence clear |
| **One notebook = one question** | Keep them focused and runnable |
| **`data/` is gitignored** | Large files don't belong in Git. Document how to obtain data in the README |
| **Commit often, with meaningful messages** | Your Git history is your lab notebook |

## 🤝 Collaborating

1. Create a branch: `git checkout -b experiment/new-model`
2. Work in a new notebook or edit existing ones
3. Push and open a Pull Request
4. CI runs your notebooks automatically
5. Collaborators review the `src/` diffs (clean Python) not the notebook JSON

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
