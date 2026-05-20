# Pre-Workshop Setup Guide

## Git & GitHub for Research Collaboration

**Please complete these steps BEFORE the workshop.** Setup takes 15-20 minutes. If you get stuck on any step, come to the workshop 15 minutes early and we'll help you.

---

## 1. Install Git

### macOS
Open Terminal and run:
```bash
git --version
```
If Git is not installed, you'll be prompted to install the Xcode Command Line Tools. Click **Install**.

Alternatively, install via Homebrew:
```bash
brew install git
```

### Windows
Download and install **Git for Windows**: https://gitforwindows.org/
- During installation, accept the defaults
- Make sure "Git Bash" is selected — you'll use this as your terminal

### Linux
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git
```

### Verify installation
```bash
git --version
# Should show something like: git version 2.45.0
```

---

## 2. Configure Git

Tell Git your name and email (these appear in your commit history):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@university.edu"
```

Set the default branch name:
```bash
git config --global init.defaultBranch main
```

Set the default editor (choose one):
```bash
# If you use VS Code:
git config --global core.editor "code --wait"

# If you use nano (simple terminal editor):
git config --global core.editor "nano"

# If you use vim:
git config --global core.editor "vim"
```

---

## 3. Create a GitHub Account

If you don't already have one:
1. Go to https://github.com
2. Click **Sign Up**
3. Use your university email (this helps with free student benefits later)

### Recommended: GitHub Student Developer Pack
Apply at https://education.github.com/pack — gives you free access to GitHub Copilot, private repos, and many other developer tools.

---

## 4. Set Up Authentication

You need to authenticate your laptop with GitHub so you can push code. Choose **one** of these methods:

### Option A: GitHub CLI (Recommended — Easiest)

Install the GitHub CLI:
```bash
# macOS
brew install gh

# Windows (winget)
winget install --id GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

Then authenticate:
```bash
gh auth login
```
Follow the prompts:
- Account: **GitHub.com**
- Protocol: **HTTPS**
- Authenticate: **Login with a web browser**

Verify it works:
```bash
gh auth status
```

### Option B: SSH Key

```bash
# Generate a key (press Enter at all prompts to accept defaults)
ssh-keygen -t ed25519 -C "your.email@university.edu"

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your key
ssh-add ~/.ssh/id_ed25519

# Copy your public key
# macOS:
cat ~/.ssh/id_ed25519.pub | pbcopy
# Linux:
cat ~/.ssh/id_ed25519.pub
# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub | clip
```

Then add the key to GitHub:
1. Go to https://github.com/settings/keys
2. Click **New SSH key**
3. Paste your public key
4. Save

Test it:
```bash
ssh -T git@github.com
# Should say: "Hi username! You've successfully authenticated"
```

---

## 5. Install a Text Editor

If you don't already have a preferred code editor, install **VS Code**:
- Download: https://code.visualstudio.com/
- It's free, works on all platforms, and has excellent Git integration

---

## 6. Verify Everything Works

Run through this final checklist:

```bash
# Git is installed
git --version

# Git knows who you are
git config user.name
git config user.email

# You can authenticate with GitHub (pick one)
gh auth status          # if using GitHub CLI
ssh -T git@github.com   # if using SSH
```

If all three work, you're ready! 🎉

---

## Troubleshooting

**"git: command not found"**
- Make sure you've installed Git and restarted your terminal

**"Permission denied (publickey)"**
- Your SSH key isn't set up correctly. Try Option A (GitHub CLI) instead — it's simpler.

**"gh: command not found"**
- Make sure you've installed the GitHub CLI and restarted your terminal

**"remote: Repository not found"**
- Double-check the repository URL and your permissions

**Windows users: "which terminal should I use?"**
- Use **Git Bash** (installed with Git for Windows). It gives you a Unix-like terminal that all the workshop commands will work in.

---

## Need Help?

If you're stuck, don't worry — come to the workshop 15 minutes early and we'll get you sorted. You can also email [INSTRUCTOR EMAIL] with a screenshot of the error.

### Can't get local setup working?

If all else fails, you can use **GitHub Codespaces** — a full development environment in your browser, no local installation needed. It's free for verified students (180 hours/month through the Student Developer Pack).

1. Go to any GitHub repository
2. Click the green **Code** button
3. Click **Codespaces → New codespace**
4. You'll have a full terminal + editor in ~60 seconds

This is a great backup plan, but we recommend local setup if possible — it's the environment you'll use day-to-day in your research.
