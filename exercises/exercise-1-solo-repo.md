# Exercise 1: Create Your Research Repository

**Time: 10 minutes**

## Your Task

Create a Git repository for a mock research project. Pick any topic you're interested in — it doesn't need to be real data or working code.

## Steps

### 1. Create a project folder
```bash
mkdir my-research-project
cd my-research-project
git init
```

### 2. Create a `README.md`
Use your text editor to create a file called `README.md` with:
- A project title
- A one-line description of the research
- Your name

### 3. Make your first commit
```bash
git add README.md
git commit -m "Add project README"
```

### 4. Create a Python script
Create a file (e.g., `analysis.py` or `process_data.py`) with a few functions. It doesn't need to run — just something plausible:

```python
"""My analysis module."""

def load_data(filepath):
    """Load raw data from file."""
    pass

def clean_data(df):
    """Remove invalid entries."""
    pass
```

```bash
git add analysis.py
git commit -m "Add initial analysis script with data loading functions"
```

### 5. Create a `.gitignore`
```
data/*.csv
.ipynb_checkpoints/
__pycache__/
.DS_Store
.env
```

```bash
git add .gitignore
git commit -m "Add .gitignore for data files and Python artifacts"
```

### 6. Check your history
```bash
git log --oneline
```

You should see 3 commits with meaningful messages. 🎉

---

## Finished Early?

Try these:
- `git log --graph --all --oneline` — visual history (more interesting once we add branches!)
- `git diff HEAD~2` — see what changed over the last 2 commits
- Edit a file, then run `git diff` BEFORE staging — see the working directory diff
- Add more files and commits — a notebook, a config file, a `docs/` folder
