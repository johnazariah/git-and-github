# GitHub Copilot — Your AI Pair Programmer for Git

## What Is GitHub Copilot?

GitHub Copilot is an AI assistant that understands Git, GitHub, and programming. It can explain commands, suggest solutions, debug problems, and walk you through complex Git operations — right in your terminal or editor.

Think of it as having a senior developer available 24/7 when you're stuck at midnight before a deadline.

---

## How to Get Access (Free for Students!)

1. **Apply for the GitHub Student Developer Pack**
   - Go to: **https://education.github.com/pack**
   - Sign in with your GitHub account
   - Verify your student status with your university email or student ID
   - Approval is usually within a few days

2. **Install the GitHub CLI** (if you haven't already)
   ```bash
   # macOS
   brew install gh

   # Windows
   winget install --id GitHub.cli

   # Linux
   sudo apt install gh
   ```

3. **Install the Copilot CLI extension**
   ```bash
   gh extension install github/gh-copilot
   ```

4. **Authenticate**
   ```bash
   gh auth login
   ```

---

## Using Copilot in the Terminal

### Ask for a Git command

```bash
gh copilot suggest "how do I undo my last commit but keep the changes"
```

### Get an explanation of a command

```bash
gh copilot explain "git rebase -i HEAD~3"
```

---

## 5 Prompts Every Researcher Should Know

### 1. "I committed a huge data file — help!"
```bash
gh copilot suggest "I accidentally committed a 500MB CSV file. How do I remove it from my git history?"
```

### 2. "How do I go back to a previous version?"
```bash
gh copilot suggest "I want to see what my analysis.py looked like 5 commits ago"
```

### 3. "I'm getting a merge conflict and I'm lost"
```bash
gh copilot suggest "I have a merge conflict in analysis.py. Walk me through resolving it step by step"
```

### 4. "I want to save my current work without committing"
```bash
gh copilot suggest "how do I temporarily save my changes and switch to another branch"
```

### 5. "How do I tag my code for a paper submission?"
```bash
gh copilot suggest "I want to mark the current state of my repo as the version I submitted to a journal"
```

---

## Copilot in VS Code

If you use VS Code, Copilot also works in the editor:

1. Install the **GitHub Copilot** extension from the VS Code marketplace
2. Sign in with your GitHub account
3. Copilot will suggest code completions as you type
4. Use **Copilot Chat** (sidebar) to ask questions about your code, get explanations, or debug errors

---

## Tips

- **Be specific** in your prompts — "how do I undo a commit" is good, "fix git" is too vague
- **Copilot explains its reasoning** — read the explanations, don't just copy commands
- **It knows your context** — you can ask follow-up questions
- **It's not perfect** — always understand what a command does before running it, especially anything with `--force` or `reset --hard`

---

## Learn More

- GitHub Copilot docs: **https://docs.github.com/copilot**
- GitHub Student Developer Pack: **https://education.github.com/pack**
- Copilot CLI usage: **https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line**
