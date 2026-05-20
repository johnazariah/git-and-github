# Git & GitHub Cheat Sheet — For Researchers

## Getting Started

| Command | What It Does |
|---------|-------------|
| `git init` | Start tracking a folder with Git |
| `git clone <url>` | Download a repo from GitHub to your laptop |
| `git status` | See what's changed (run this often!) |

## The Core Workflow

```
 Edit files → git add → git commit → git push
              (stage)    (snapshot)   (upload)
```

| Command | What It Does |
|---------|-------------|
| `git add <file>` | Stage a file for the next snapshot |
| `git add .` | Stage everything that's changed |
| `git commit -m "message"` | Save a snapshot with a description |
| `git push` | Upload your snapshots to GitHub |
| `git pull` | Download your collaborator's changes |

## Seeing History

| Command | What It Does |
|---------|-------------|
| `git log --oneline` | Compact list of all snapshots |
| `git log --oneline --graph --all` | Visual branch diagram |
| `git diff` | See what you changed (before staging) |
| `git diff --staged` | See what's about to be committed |
| `git diff HEAD~2` | Compare with 2 commits ago |

## Branching & Collaboration

| Command | What It Does |
|---------|-------------|
| `git branch` | List branches (* = current) |
| `git checkout -b <name>` | Create a new branch and switch to it |
| `git checkout main` | Switch back to main |
| `git push origin <branch>` | Push a branch to GitHub |
| `git merge <branch>` | Merge a branch into current branch |

## Resolving Merge Conflicts

When Git can't auto-merge, it marks the file:

```
<<<<<<< HEAD
Your version of the line
=======
Their version of the line
>>>>>>> branch-name
```

**To resolve:** Edit the file to keep what you want, remove the markers, then:
```bash
git add <file>
git commit -m "Resolve merge conflict in <file>"
```

## Undoing Things

| Command | What It Does |
|---------|-------------|
| `git checkout -- <file>` | Discard uncommitted changes to a file |
| `git reset HEAD <file>` | Unstage a file (keep changes) |
| `git revert <commit>` | Create a new commit that undoes a previous one |

⚠️ **When in doubt, ask before you force-push.** `git push --force` rewrites history and can destroy your collaborator's work.

---

## Commit Message Guide

### ✅ Good Messages
```
Add regression analysis for hypothesis 2
Fix off-by-one error in date range filtering
Clean temperature data: remove stations with >30% missing
Update README with methods section and citation
```

### ❌ Bad Messages
```
update
fix
asdf
changes
WIP
```

**Formula:** Start with a verb. Say what AND why.

---

## Research-Specific Patterns

### Branch Naming for Research
```
experiment/new-regression-model
feature/add-visualisation
fix/data-cleaning-bug
docs/update-methods-section
```

### Tagging Submissions
```bash
git tag -a v1.0-submitted-to-nature -m "Submitted to Nature, May 2026"
git push origin --tags
```

### Getting a DOI for Your Code
1. Connect your GitHub repo to **Zenodo** (zenodo.org)
2. Create a **Release** on GitHub
3. Zenodo automatically archives it and assigns a DOI
4. Add the DOI badge to your README

---

## Git + Jupyter Notebooks

Notebooks (`.ipynb`) are stored as JSON, which makes Git diffs messy.

### Tips
- **Strip output before committing**: Use `nbstripout` to automatically remove cell outputs
  ```bash
  pip install nbstripout
  nbstripout --install    # sets up a Git filter automatically
  ```
- **Always add to `.gitignore`**:
  ```
  .ipynb_checkpoints/
  ```
- **Consider `jupytext`**: Syncs notebooks with plain `.py` files for cleaner diffs
  ```bash
  pip install jupytext
  jupytext --set-formats ipynb,py:percent notebook.ipynb
  ```
- **Rule of thumb**: Use notebooks for exploration, `.py` files for reusable functions

---

## .gitignore Essentials for Research

```gitignore
# Large data files
data/*.csv
data/*.h5
*.parquet

# Notebook checkpoints
.ipynb_checkpoints/

# Python environment
__pycache__/
*.pyc
.venv/

# Secrets and credentials
.env
credentials.json

# OS clutter
.DS_Store
Thumbs.db
```

**Generate a starter `.gitignore`**: https://www.toptal.com/developers/gitignore

---

## Useful GitHub Features

| Feature | How It Helps Research |
|---------|----------------------|
| **Issues** | Track experiments, TODOs, bugs |
| **Pull Requests** | Propose and review changes with collaborators |
| **Pages** | Publish project documentation as a website |
| **Actions** | Automate tests, builds, deployments on every push |
| **Releases** | Archive specific versions (great for paper submissions) |
| **Organizations** | Set up a shared space for your lab group |

---

## Getting Help

| Resource | URL |
|----------|-----|
| Pro Git book (free) | git-scm.com/book |
| GitHub Skills | skills.github.com |
| Software Carpentry Git lesson | swcarpentry.github.io/git-novice |
| GitHub Docs | docs.github.com |
| `git help <command>` | Built-in help in your terminal |
