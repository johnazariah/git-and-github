# Exercise 2: Collaboration — Research Team Simulation

**Time: 25 minutes (Round 1: 10 min, Round 2: 10 min, Debrief: 5 min)**

Pair up with someone near you. Decide who is **Person A** and who is **Person B**.

---

## Setup (3 minutes)

### Person A:
1. Go to **GitHub** → **New Repository** → name it `collab-research`
2. Clone it locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/collab-research.git
   cd collab-research
   ```
3. Copy the template files (provided by instructor) into this folder
4. Commit and push:
   ```bash
   git add .
   git commit -m "Add initial project files"
   git push
   ```
5. Go to repo **Settings → Collaborators → Add people** → add Person B's GitHub username

### Person B:
1. **Accept the invitation** (check your email or GitHub notifications bell 🔔)
2. Clone the repo:
   ```bash
   git clone https://github.com/PERSON-A-USERNAME/collab-research.git
   cd collab-research
   ```

✅ Both of you should now have the same files locally.

---

## Round 1: Parallel Work — The Happy Path (10 minutes)

You'll each work on a **different file** so there's no conflict.

### Person A: Improve the analysis

```bash
git checkout -b feature/improve-analysis
```

Edit `analysis.py` — add a new function at the bottom:

```python
def calculate_seasonal_averages(df):
    """Group temperatures by season and calculate means."""
    seasons = {12: 'Summer', 1: 'Summer', 2: 'Summer',
               3: 'Autumn', 4: 'Autumn', 5: 'Autumn',
               6: 'Winter', 7: 'Winter', 8: 'Winter',
               9: 'Spring', 10: 'Spring', 11: 'Spring'}
    df = df.copy()
    df['season'] = df['date'].dt.month.map(seasons)
    return df.groupby(['station', 'season'])['temperature'].mean()
```

```bash
git add analysis.py
git commit -m "Add seasonal averages calculation"
git push origin feature/improve-analysis
```

Go to GitHub → open a **Pull Request**.

### Person B: Update the documentation

```bash
git checkout -b feature/update-docs
```

Edit `README.md` — add a Methods section after "Project Overview":

```markdown
## Methods

We use linear regression to detect long-term temperature trends and
seasonal decomposition to identify cyclical patterns. Data cleaning
removes stations with more than 20% missing values.
```

```bash
git add README.md
git commit -m "Add methods section to README"
git push origin feature/update-docs
```

Go to GitHub → open a **Pull Request**.

### Both: Review and Merge

1. Go to your partner's Pull Request
2. Click **Files changed** — read what they did
3. Leave **at least one comment** on a specific line (click the `+` button next to a line)
4. Click **Review changes → Approve → Submit review**
5. Click **Merge pull request**

✅ Both PRs should now be merged into `main`.

---

## Round 2: The Merge Conflict (10 minutes)

Now you'll both edit the **same line** of the same file. This will create a merge conflict — and that's the point!

### Both people:
```bash
git checkout main
git pull origin main
```

You should both now have the merged changes from Round 1.

### Person A:
```bash
git checkout -b experiment/method-a
```
Edit **line 1** of `analysis.py` to:
```python
"""Analysis module — Method A: Linear Regression"""
```
```bash
git add analysis.py
git commit -m "Set analysis method to Linear Regression"
git push origin experiment/method-a
```
Go to GitHub → open a PR → **merge it immediately**.

### Person B:
```bash
git checkout -b experiment/method-b
```
Edit **line 1** of `analysis.py` to:
```python
"""Analysis module — Method B: Random Forest"""
```
```bash
git add analysis.py
git commit -m "Set analysis method to Random Forest"
git push origin experiment/method-b
```
Go to GitHub → open a PR.

⚠️ **You'll see a merge conflict!** GitHub will say this branch has conflicts that must be resolved.

### Person B: Resolve the conflict

```bash
# Pull the latest main into your branch
git checkout experiment/method-b
git pull origin main
```

Git will tell you there's a conflict. Open `analysis.py` — you'll see something like:

```
<<<<<<< HEAD
"""Analysis module — Method B: Random Forest"""
=======
"""Analysis module — Method A: Linear Regression"""
>>>>>>> main
```

**Edit the file** to keep what you want (or combine them!). Remove the `<<<<<<<`, `=======`, and `>>>>>>>` markers. For example:

```python
"""Analysis module — Method B: Random Forest (Alternative to Linear Regression)"""
```

Then:
```bash
git add analysis.py
git commit -m "Resolve merge conflict: keep Random Forest method"
git push origin experiment/method-b
```

Go back to your PR on GitHub — it should now be mergeable! ✅

---

## Debrief Discussion

- How did the merge conflict feel?
- How would you prevent conflicts in a real project?
- What role do pull requests play in research collaboration?

**Key takeaway:** Merge conflicts aren't errors — they're Git asking you to make a decision. Communication with your collaborators prevents most of them.
