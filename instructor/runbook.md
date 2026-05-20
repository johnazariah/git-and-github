# Git & GitHub for Research Collaboration — Instructor Runbook

> **Duration:** 2 hours  
> **Audience:** 20–30 STEM graduate students (mixed skill levels)  
> **Format:** In-person, students on own laptops  
> **Instructor setup:** Solo instructor, no TAs

---

## Pre-Workshop Checklist (Day Before)

- [ ] Send/resend the [Pre-Workshop Setup Guide](../pre-workshop/setup-guide.md) — emphasise that setup is **required**
- [ ] Test your screen sharing / projector with terminal + browser side-by-side
- [ ] Create the **demo repository** on your GitHub account (`research-demo-2026`)
- [ ] Have the [template repo files](../exercises/template-repo/) ready to push or share
- [ ] Print handouts: [Git Cheat Sheet](../handouts/git-cheatsheet.md), [Copilot One-Pager](../handouts/copilot-one-pager.md)
- [ ] Pre-stage the Copilot demo scenario (see Block 6)
- [ ] Have a backup plan for auth issues: HTTPS clone URLs + `gh auth login` as fallback
- [ ] Load this runbook on a second screen or tablet so you can glance at it

### Room Setup
- Arrive 15 min early
- Write on whiteboard/slide: **WiFi credentials**, **your GitHub username**, and the URL to the pre-workshop setup guide
- Have a "parking lot" area on the board for questions you'll address later

---

## Block 1: Why Version Control Matters for Research (10 min)

### Timing
| Segment | Duration |
|---------|----------|
| The horror story | 3 min |
| What Git actually does | 3 min |
| Research motivations + show a real repo | 4 min |

### Talking Points

**Open with engagement (1 min):**
> "Quick show of hands — who has a file on their computer right now called something like `analysis_final_v2_REAL_FINAL.py`?"

Wait for laughs. Follow up:
> "Who has emailed a script to a collaborator and then lost track of which version is current?"

**The problem (2 min):**
- Research involves constant iteration — you try things, back up, try again
- Without version control, your options are: copy folders, rename files, or pray
- Collaboration makes it 10× worse — who changed what? when? why?

**What Git does (3 min):**
- Git takes **snapshots** of your project at moments you choose
- Every snapshot has a message explaining *what changed and why*
- You can go back to any snapshot, compare any two, branch off in different directions
- Mental model: **Git is a lab notebook for your code and analysis**

**Why researchers specifically need this (4 min):**
- **Reproducibility**: Reviewer asks "how exactly did you generate Figure 3?" → you can point to the exact snapshot
- **Collaboration with a trail**: Your supervisor can see what you changed, when, and why — no more "I think I updated the regression last Tuesday?"
- **Journal requirements**: Many journals now require code/data repositories (Nature, PLOS, etc.)
- **Show a real example**: Pull up a published paper's companion GitHub repo
  - Suggestions: any repo linked from a Nature paper, or search GitHub for "companion code" + your field
  - Point out: README as documentation, commit history as a timeline, releases tagged to paper versions

### Instructor Notes
- Don't oversell — be honest that Git has a learning curve. "It will feel weird for about a week, then you'll wonder how you lived without it."
- If someone asks about Google Docs/Overleaf: "Those are great for documents. Git is for code, scripts, data pipelines, config files — the computational side of your research."

---

## Block 2: Git Fundamentals — Solo Workflow (30 min)

### Timing
| Segment | Duration |
|---------|----------|
| Live coding: init → commit cycle | 15 min |
| .gitignore | 5 min |
| Solo exercise | 10 min |

### Setup
- Have your terminal and a text editor visible side-by-side
- Use a large font (≥16pt in terminal)
- Create a fresh directory for the demo — don't reuse an existing repo

### Live Coding Script

**Create the project (narrate every step):**

```bash
# "Let's say we're starting a new research project on climate data analysis"
mkdir climate-analysis
cd climate-analysis

# "First, we tell Git to start tracking this folder"
git init

# "Git is now watching this folder. Let's check the status"
git status
# Point out: "On branch main, nothing to commit"
```

**First commit — the README:**

```bash
# Create a README (use your editor, or echo for speed)
# Write 2-3 lines: project title, one-line description, your name
```

```markdown
# Climate Data Analysis
Analysing historical temperature trends in Australian capital cities.
Author: [Your Name]
```

```bash
git status
# Point out: "Untracked files" — Git sees the file but isn't tracking it yet

git add README.md
git status
# Point out: "Changes to be staged" — now it's in the staging area, ready to be saved

git commit -m "Add project README with description"
# Explain: the -m flag is the message. It should say WHAT and WHY, not just "update"
```

> **Pause and explain the mental model:**
> "There are three zones: your **working directory** (where you edit), the **staging area** (where you prepare a snapshot), and the **repository** (the saved snapshots). `add` moves things to staging. `commit` saves the snapshot."

**Second commit — a data cleaning script:**

Create a simple Python script:

```python
# clean_data.py
"""Clean and prepare raw temperature data for analysis."""
import pandas as pd

def load_raw_data(filepath):
    """Load raw CSV temperature data."""
    df = pd.read_csv(filepath)
    return df

def remove_outliers(df, column, std_threshold=3):
    """Remove values more than std_threshold standard deviations from mean."""
    mean = df[column].mean()
    std = df[column].std()
    return df[abs(df[column] - mean) <= std_threshold * std]

if __name__ == "__main__":
    data = load_raw_data("data/raw_temperatures.csv")
    cleaned = remove_outliers(data, "temperature")
    cleaned.to_csv("data/cleaned_temperatures.csv", index=False)
    print(f"Cleaned {len(data)} rows to {len(cleaned)} rows")
```

```bash
git add clean_data.py
git commit -m "Add data cleaning script with outlier removal"
```

**Third commit — a notebook for exploration:**

Create a simple notebook file (or have one prepared). Explain:

> "Many of you work in Jupyter notebooks. Let's add one."

```bash
# Add a pre-made notebook (have this ready)
cp ~/workshop-materials/explore.ipynb .
git add explore.ipynb
git commit -m "Add exploratory analysis notebook"
```

**Now show them the history and diffs:**

```bash
git log --oneline
# "See? Three snapshots, each with a clear message. This is your lab notebook."

git diff HEAD~1
# "This shows what changed in the last commit"
# Point out: the notebook diff is ugly JSON — we'll talk about that
```

> **Key moment — the notebook diff:**
> "See this mess? Notebooks are stored as JSON, so Git diffs are hard to read. This is important — we'll talk about strategies for this. For now, know that plain `.py` files give you much cleaner diffs."

### .gitignore (5 min)

```bash
# "Before we go further — there are files Git should NEVER track"
```

Create `.gitignore`:

```
# Data files (too large for Git)
data/*.csv
data/*.h5
*.parquet

# Notebook checkpoints
.ipynb_checkpoints/

# Python
__pycache__/
*.pyc
.venv/

# OS files
.DS_Store
Thumbs.db

# Secrets
.env
credentials.json
```

```bash
git add .gitignore
git commit -m "Add .gitignore for data files, notebooks checkpoints, and secrets"
```

> **Emphasise:**
> "Rule of thumb: if it's **generated**, **large**, or **secret**, it goes in `.gitignore`. Your 2GB dataset does NOT belong in Git. Your API keys DEFINITELY don't belong in Git."

### Solo Exercise (10 min)

Display on screen:

> **Exercise: Create Your Research Repo (10 min)**
>
> 1. Create a new folder for a mock research project (pick any topic you like)
> 2. `git init` inside it
> 3. Create a `README.md` describing the project (2-3 lines is fine)
> 4. Create at least one Python script (`.py`) — it can be simple
> 5. Create a `.gitignore` appropriate for your project
> 6. Make at least **3 commits** with meaningful messages
> 7. Run `git log --oneline` to see your history
>
> **Finished early?** Try:
> - `git log --graph --all --oneline` (will be more interesting later)
> - `git diff HEAD~2` to see changes across multiple commits
> - Edit a file, then try `git diff` before staging it

**Walk the room** during this exercise. Common issues:
- Not `cd`-ing into the directory before `git init`
- Forgetting `git add` before `commit`
- Commit messages like "asdf" — gently encourage meaningful ones
- Students who are stuck: sit with them for 30 seconds, don't just point at the screen

---

## Block 3: GitHub — Your Research Portfolio + Pages (20 min)

### Timing
| Segment | Duration |
|---------|----------|
| Push to GitHub | 8 min |
| GitHub tour + turn on Pages | 7 min |
| Students push their repos + Pages reveal | 5 min |

### Push to GitHub

```bash
# "Now let's put this on GitHub so it exists beyond your laptop"
```

**On GitHub (browser):**
1. Click **New Repository**
2. Name: `climate-analysis` (match the local folder)
3. **Do NOT** initialise with README (we already have one)
4. Create

**Back in terminal:**

```bash
git remote add origin https://github.com/YOUR-USERNAME/climate-analysis.git
git branch -M main
git push -u origin main
```

> **Explain the mental model:**
> "Your laptop has a copy. GitHub now has a copy. `push` sends your snapshots to GitHub. `pull` brings others' changes back down. They stay in sync through these commands."

**If auth issues arise:**
- HTTPS: `gh auth login` is the fastest fix
- SSH: if they set it up in pre-workshop, it should work
- Don't spend more than 2 min on any one person's auth issue — note it and move on

### GitHub Tour (5 min)

In the browser, show:
- **README renders automatically** — "This is your project's landing page"
- **Commit history** — "Click any commit to see exactly what changed"
- **Issues tab** — "Use this to track TODOs, experiment ideas, bugs. Way better than a text file."
- **Create a quick Issue**: "TODO: Add visualisation for temperature trends" — show labels, assignment

### Turn on GitHub Pages (2 min)

> "Now I'm going to show you something that takes 30 seconds and will blow your mind."

1. **Settings → Pages**
2. Source: **GitHub Actions** (or Deploy from branch → `main`, `/root`)
3. Save

> "GitHub is now building a website from your repo. It takes about a minute. Let's keep going and check back."

### Students Push + Pages Moment (5 min)

> "Everyone: push your exercise repo to GitHub now. Once it's up, go to Settings → Pages and turn it on."

Give them 3-4 minutes. Then:

> "OK, check your Pages URL — it's `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`. What do you see?"

They should see their README rendered as a web page.

> "You just published a website by pushing a Git commit. That green checkmark in the Actions tab? That's a **GitHub Action** that ran automatically to build and deploy your site. You can set up Actions to do anything on every push — run tests, validate data, build documentation, regenerate figures. For now, just know it's there."

### Instructor Notes
- The Pages URL takes 30-60 seconds to go live. If it's not ready, say "give it another minute" and move on.
- Some students may not have a README that renders well — that's fine, the point is the mechanism.
- If you want a more impressive demo, have a pre-built repo with a nicer README (badges, images, sections) to show what's possible.

---

## Block 4: Branching & Collaboration (40 min) ⭐

### Timing
| Segment | Duration |
|---------|----------|
| Branching concepts + demo | 10 min |
| Pull request walkthrough | 5 min |
| Collaboration exercise — Round 1 (happy path) | 10 min |
| Collaboration exercise — Round 2 (merge conflict) | 10 min |
| Debrief | 5 min |

### Branching Concepts (10 min)

> "So far, everything has been on one line — `main`. But real research isn't linear. You want to try a different model, test a new approach, without risking your working code."

**Live demo:**

```bash
# "Let's say I want to try a different outlier detection method"
git checkout -b experiment/zscore-outliers

# Make a change to clean_data.py — modify the remove_outliers function
# (change the approach, e.g., use IQR instead of std deviation)
```

```python
def remove_outliers(df, column):
    """Remove outliers using IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)]
```

```bash
git add clean_data.py
git commit -m "Experiment: try IQR method for outlier removal"

# Show the branch structure
git log --oneline --graph --all
# "See? main is untouched. Our experiment is on a separate branch."

# Switch back to main
git checkout main
# "Look — our original code is still here, unchanged"
cat clean_data.py

# Switch back to the experiment
git checkout experiment/zscore-outliers
# "And our experiment is still here"
```

> **Mental model:**
> "Think of branches as parallel universes. `main` is your stable reality. Branches are experiments. If the experiment works, you merge it into your reality. If it doesn't, you just delete the branch — no harm done."

### Pull Request Walkthrough (5 min)

```bash
git push origin experiment/zscore-outliers
```

**In browser:**
1. GitHub shows "compare & pull request" banner — click it
2. Write a PR description: "Testing IQR method vs. standard deviation for outlier detection. Initial results look promising — fewer false positives on the Melbourne dataset."
3. Show the **Files changed** tab — "Your collaborator can see exactly what you changed"
4. Show **line commenting** — click a line, leave a comment: "Should we parameterise the 1.5× multiplier?"
5. Show **approve and merge**

> "This is how research collaboration works on GitHub. You don't email code. You open a pull request, discuss it, and merge when everyone's happy."

### Collaboration Exercise Setup

**Display on screen:**

> **Collaboration Exercise: Research Team Simulation**
>
> **Pair up** with someone near you (groups of 3 are fine if odd numbers).
>
> **Setup (2 min):**
> 1. **Person A**: Go to GitHub → Create a new repo called `collab-research`
> 2. **Person A**: Clone it locally, copy in the [template files](we'll provide the URL), commit, and push
> 3. **Person A**: Go to repo Settings → Collaborators → Add Person B's GitHub username
> 4. **Person B**: Accept the invitation (check email or GitHub notifications) and clone the repo
>
> If stuck, raise your hand. Don't spend more than 3 minutes on setup.

**Have the template repo URL on screen** — students should download/copy these files into their repo:
- `README.md` — project description
- `analysis.py` — a simple analysis script
- `explore.ipynb` — an exploration notebook
- `requirements.txt` — dependencies

### Round 1: The Happy Path (10 min)

**Display on screen:**

> **Round 1: Parallel Work (10 min)**
>
> Each person creates a branch and makes a change to a **different file**:
>
> - **Person A**: Create branch `feature/improve-analysis`
>   - Edit `analysis.py` — add a new function (anything you like)
>   - Commit and push your branch
>   - Open a Pull Request on GitHub
>
> - **Person B**: Create branch `feature/update-docs`
>   - Edit `README.md` — add a "Methods" section
>   - Commit and push your branch
>   - Open a Pull Request on GitHub
>
> Then **review each other's PR** — leave at least one comment. Approve and merge.
>
> ```bash
> # Quick reference:
> git checkout -b feature/your-branch-name
> # ... make changes ...
> git add .
> git commit -m "Your message"
> git push origin feature/your-branch-name
> # Then go to GitHub to open the PR
> ```

**Walk the room.** Common issues:
- Forgetting to push the branch (they push `main` instead)
- Not seeing the "Compare & Pull Request" button — tell them to click the branch dropdown
- Permission issues — make sure Person A actually added Person B as collaborator

### Round 2: The Merge Conflict (10 min)

> "OK, that was the happy path. Now let's see what happens when two people edit the same thing."

**Display on screen:**

> **Round 2: The Merge Conflict (10 min)**
>
> Both of you will edit the **same line** of `analysis.py`:
>
> 1. Both: `git checkout main` and `git pull origin main` (get the merged changes)
> 2. **Person A**: Create branch `experiment/method-a`, change line 1 of `analysis.py` to:
>    `"""Analysis module — Method A: Linear Regression"""`
> 3. **Person B**: Create branch `experiment/method-b`, change line 1 of `analysis.py` to:
>    `"""Analysis module — Method B: Random Forest"""`
> 4. **Person A**: Push, open PR, merge it first
> 5. **Person B**: Push, open PR — you'll see a **merge conflict**!
>
> **To resolve the conflict:**
> ```bash
> git checkout experiment/method-b
> git pull origin main
> # Git will tell you there's a conflict — open the file
> # You'll see <<<<<<< and >>>>>>> markers
> # Edit the file to keep what you want, remove the markers
> git add analysis.py
> git commit -m "Resolve merge conflict: keep Method B"
> git push origin experiment/method-b
> # The PR on GitHub should now be mergeable
> ```

**Have the conflict resolution steps displayed on screen throughout.**

> "Merge conflicts feel scary but they're just Git saying 'I found two changes to the same spot and I don't know which one you want — you decide.' It's a conversation, not an error."

**Walk the room actively during this exercise.** Merge conflicts are where people get stuck. Spend time with struggling pairs. If someone is really stuck, resolve it together on their screen.

### Debrief (5 min)

> "How did that feel?"

Let a few people respond. Then:

> "Conflicts are normal. They happen in every research team. The important thing is: Git caught the conflict instead of silently overwriting someone's work. That's the whole point."
>
> "In real life, you minimise conflicts by: working on different files when possible, pulling often, and communicating with your team about who's working on what."

---

## Block 5: Research Workflow Patterns (5 min)

### Quick-Fire Tips

> "Let me rapid-fire some patterns that will save you pain:"

1. **Commit early, commit often** — "After every logical step: cleaned data, ran analysis, fixed a bug. Not 'end of day dump everything.'"

2. **Write meaningful messages** — "Future you will thank present you."
   - Bad: `"update"`, `"fix"`, `"asdf"`
   - Good: `"Add regression analysis for hypothesis 2"`, `"Fix off-by-one error in date parsing"`

3. **Branch naming** — `experiment/new-model`, `fix/data-cleaning-bug`, `feature/add-visualisation`

4. **Tag your submissions** — `git tag v1.0-submitted-to-nature` — marks the exact snapshot you submitted

5. **GitHub + Zenodo** — "You can get a DOI for your GitHub repo. Cite your code like a paper."

> "The cheat sheet I'm handing out has all of these plus notebook-specific tips."

---

## Block 6: Copilot Demo & Wrap-up (10 min)

### Timing
| Segment | Duration |
|---------|----------|
| Copilot demo | 5 min |
| Resources + Q&A | 5 min |

### Copilot Demo (5 min)

**Setup (do this before the workshop):**
- Have a repo with a large file committed (or fake it with the scenario)
- Have GitHub Copilot CLI installed and authenticated

**The scenario:**

> "OK, it's midnight. Your paper deadline is tomorrow. You just realised you accidentally committed a 500MB data file and pushed it. Git won't let you push anymore because the file is too large. You're panicking. What do you do?"

> "Well, you could Google it and read 17 Stack Overflow answers... or:"

**In your terminal:**

```bash
# Ask Copilot
gh copilot suggest "I accidentally committed a large data file to my repo and pushed it. How do I remove it from the git history completely?"
```

Show Copilot walking through the solution. React naturally:

> "See? It's giving me the exact commands, explaining what each one does, and warning me about the consequences. This is like having a senior developer sitting next to you at midnight."

> "One more — something simpler:"

```bash
gh copilot explain "git rebase -i HEAD~3"
```

> "You don't need to memorise everything. You need to understand the concepts — which you now do — and know where to get help."

**Transition to handout:**

> "Now, Copilot requires a subscription or GitHub Education access. I'm handing out a one-pager that shows you how to get access through the GitHub Student Developer Pack — it's free for students — and gives you example prompts for common research Git problems."

### Resources & Q&A (5 min)

**Hand out:**
- [Git Cheat Sheet](../handouts/git-cheatsheet.md)
- [Copilot One-Pager](../handouts/copilot-one-pager.md)

> "Resources to continue learning:"
> - **Pro Git book** (free): git-scm.com/book
> - **GitHub Skills**: skills.github.com (interactive courses)
> - **Software Carpentry Git lesson**: great for researchers specifically
>
> "What questions do you have?"

Take questions for remaining time. Common ones:
- "How do I handle large datasets?" → Git LFS, or keep data separate and reference it
- "Should I make my repo public?" → Discuss open science, embargoes, licensing
- "How does this work with Overleaf/LaTeX?" → Git integration exists, or use Git for code + Overleaf for writing

---

## Emergency Procedures

### If WiFi goes down
- You can still teach Git locally (Blocks 1-2 work offline)
- Skip the push/Pages/collaboration and focus on solo Git + workflow patterns
- Show GitHub features from screenshots on your local machine

### If many students can't authenticate with GitHub
- Have `gh auth login` as the universal fix
- HTTPS clone URLs as fallback
- Worst case: have one student share their screen for the collaboration demo, others follow conceptually

### If you're running behind
- **Cut first**: Block 5 (workflow patterns → move to handout)
- **Cut second**: Round 2 of collaboration exercise (merge conflict → just demo it yourself)
- **Never cut**: Block 4 Round 1 (the collaboration exercise is the centrepiece)
- **Never cut**: The solo exercise in Block 2 (they need to feel the muscle memory)

### If you're running ahead
- Expand Q&A
- Do a live demo of creating a GitHub Issue, linking it to a branch, and closing it via commit message
- Show `git stash` as a bonus concept
- Deeper dive into GitHub Actions — show a simple CI YAML file
