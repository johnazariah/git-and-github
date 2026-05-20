# Pre-Workshop Setup Guide

## Git & GitHub for Research Collaboration

**Please complete these steps BEFORE the workshop.** The full setup takes about 30 minutes. If you get stuck on any step, come to the workshop 15 minutes early and we'll help you.

> **Already comfortable with Git and GitHub?** Skip to the [verification checklist](#7-verify-everything-works) at the bottom to make sure everything's ready.

---

## 1. Install Git

### macOS

Open **Terminal** (search for it in Spotlight, or find it in Applications → Utilities) and run:

```bash
git --version
```

**If Git is already installed**, you'll see something like `git version 2.45.0` — you're done with this step.

**If Git is NOT installed**, you'll be prompted to install the Xcode Command Line Tools. Click **Install** and wait a few minutes.

Alternatively, if you use Homebrew:
```bash
brew install git
```

### Windows

1. Download **Git for Windows**: https://gitforwindows.org/
2. Run the installer
3. **Use the default settings** for all prompts, except:
   - Make sure **"Git Bash"** is selected (this gives you a Unix-like terminal)
   - For "Adjusting your PATH environment", select **"Git from the command line and also from 3rd-party software"**
4. After installation, open **Git Bash** (search for it in the Start menu) — this is the terminal you'll use for the workshop

> ⚠️ **Windows users**: Use **Git Bash** for all terminal commands in this guide and during the workshop. PowerShell and CMD will work for basic Git, but the commands we demonstrate assume a Bash-like shell.

### Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Verify Git is installed

```bash
git --version
```

You should see output like `git version 2.45.0` (any version 2.30+ is fine).

---

## 2. Configure Git

These settings tell Git who you are. They appear in every commit you make, so use your real name and the email associated with your GitHub account.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@university.edu"
```

Set the default branch name to `main` (the modern convention):
```bash
git config --global init.defaultBranch main
```

Set your preferred text editor for Git commit messages:
```bash
# If you use VS Code (recommended):
git config --global core.editor "code --wait"

# If you prefer nano (simple terminal editor, good for beginners):
git config --global core.editor "nano"

# If you prefer vim:
git config --global core.editor "vim"
```

**Verify your configuration:**
```bash
git config --global --list
```

You should see your name, email, default branch, and editor listed.

---

## 3. Create a GitHub Account

If you already have a GitHub account, skip to step 3b.

### 3a. Sign up

1. Go to **https://github.com**
2. Click **Sign Up**
3. **Use your university email address** (e.g., `jane.smith@university.edu`)
   - This is important — it makes it easy to verify your student status in the next step
   - You can add additional email addresses later
4. Choose a username that you're comfortable being public — this becomes part of your professional identity (e.g., `jsmith-research`, not `xXx_destroyer_xXx`)
5. Complete the sign-up process and verify your email

### 3b. Apply for the GitHub Student Developer Pack ⭐

This is **strongly recommended** — it gives you free access to:
- **GitHub Copilot** (AI coding assistant — we'll demo this in the workshop)
- **GitHub Codespaces** (cloud development environments — 180 hours/month free)
- **GitHub Pro** (unlimited private repos, advanced features)
- Dozens of other developer tools and learning resources

**How to apply:**

1. Go to **https://education.github.com/pack**
2. Click **"Get your Pack"** (or "Sign up for Student Developer Pack")
3. Select **"Student"** and your university
4. Verify your status using **one** of these methods:
   - **University email** (fastest — if your account uses a `.edu` or recognised university domain)
   - **Upload proof** — a photo of your student ID, enrolment letter, or transcript
5. Submit and wait for approval

> **Timing**: Approval typically takes a few minutes to a few days. Apply **at least a week before the workshop** if possible. If you're not approved in time, you can still do everything in the workshop — Copilot and Codespaces are bonuses, not requirements.

**How to check your status:**
- Go to https://github.com/settings/billing — if you see "GitHub Pro" under your plan, you're approved
- Or go to https://education.github.com/pack — it will show "You have the Student Developer Pack"

---

## 4. Install the GitHub CLI and Authenticate

The GitHub CLI (`gh`) is the easiest way to authenticate your laptop with GitHub. We'll also use it during the workshop.

### Install the GitHub CLI

```bash
# macOS (Homebrew)
brew install gh

# Windows (run in PowerShell as administrator, or Git Bash)
winget install --id GitHub.cli

# Ubuntu / Debian
sudo apt install gh

# If the package isn't available, see: https://github.com/cli/cli/blob/trunk/docs/install_linux.md
```

### Authenticate with GitHub

```bash
gh auth login
```

You'll see a series of prompts. Select these options:

```
? Where do you use GitHub?  →  GitHub.com
? What is your preferred protocol for Git operations?  →  HTTPS
? Authenticate Git with your GitHub credentials?  →  Yes
? How would you like to authenticate GitHub CLI?  →  Login with a web browser
```

The CLI will give you a **one-time code**. Press Enter, and your browser will open to `github.com/login/device`. Paste the code, authorize the CLI, and you're done.

**Verify it works:**
```bash
gh auth status
```

You should see:
```
github.com
  ✓ Logged in to github.com account YOUR-USERNAME
```

### Alternative: SSH Key (Advanced)

If you prefer SSH authentication (or if your institution blocks HTTPS):

```bash
# Generate a key pair
ssh-keygen -t ed25519 -C "your.email@university.edu"
# Press Enter at all prompts to accept defaults

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your key to the agent
ssh-add ~/.ssh/id_ed25519

# Copy your public key to clipboard
# macOS:
cat ~/.ssh/id_ed25519.pub | pbcopy
# Linux:
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub | clip
```

Then add the key to GitHub:
1. Go to https://github.com/settings/keys
2. Click **"New SSH key"**
3. Title: something like "My Laptop"
4. Key type: **Authentication Key**
5. Paste your public key
6. Click **"Add SSH key"**

**Test it:**
```bash
ssh -T git@github.com
# Should say: "Hi YOUR-USERNAME! You've successfully authenticated"
```

---

## 5. Install a Text Editor

If you don't already have a preferred code editor, install **Visual Studio Code (VS Code)**:

1. Download from **https://code.visualstudio.com/**
2. Install it (accept all defaults)
3. Open it and verify it runs

**Recommended VS Code extensions** (install from the Extensions panel, `Ctrl/Cmd+Shift+X`):

| Extension | Why |
|-----------|-----|
| **GitLens** | See who changed each line, rich Git history in the editor |
| **Git Graph** | Visual branch diagram |
| **Python** | If you work with Python (syntax highlighting, linting, debugging) |
| **Jupyter** | If you work with notebooks |

> Don't have VS Code? Any text editor works (Sublime Text, nano, vim). You just need to be able to edit files.

---

## 6. Set Up GitHub Copilot (Optional but Recommended)

GitHub Copilot is an AI assistant that can help you with Git commands, explain errors, and write code. We'll demo it at the end of the workshop. Setting it up now means you can start using it immediately after.

> **Prerequisite**: You need the GitHub Student Developer Pack (step 3b) or a paid Copilot subscription.

### Check if you have Copilot access

1. Go to **https://github.com/settings/copilot**
2. If you see a Copilot settings page (not a "buy" page), you have access ✅
3. If you see a purchase page, your Student Developer Pack may not be approved yet — check back later

### Install Copilot in the terminal (CLI)

```bash
# Install the Copilot extension for the GitHub CLI
gh extension install github/gh-copilot
```

**Test it:**
```bash
gh copilot explain "git status"
```

You should see Copilot explain what `git status` does. If you get an error about access, your Student Developer Pack may still be pending.

### Install Copilot in VS Code

1. Open VS Code
2. Go to the Extensions panel (`Ctrl/Cmd+Shift+X`)
3. Search for **"GitHub Copilot"** and install it
4. Search for **"GitHub Copilot Chat"** and install it
5. You'll be prompted to sign in with your GitHub account — do so
6. Once signed in, you should see a Copilot icon (✨) in the bottom status bar

> **Don't have access yet?** No worries — Copilot is a bonus, not a requirement for the workshop. We'll demo it from the stage and you can set it up afterwards.

---

## 7. Verify Everything Works

Run through this final checklist in your terminal:

```bash
echo "=== Git ==="
git --version

echo ""
echo "=== Git Config ==="
git config user.name
git config user.email

echo ""
echo "=== GitHub CLI ==="
gh auth status

echo ""
echo "=== GitHub Copilot (optional) ==="
gh copilot --version 2>/dev/null || echo "Not installed (that's OK)"
```

### ✅ You're ready if:
- [ ] `git --version` shows 2.30 or higher
- [ ] `git config user.name` shows your name
- [ ] `git config user.email` shows your email
- [ ] `gh auth status` shows you're logged in

### 🌟 Bonus points if:
- [ ] GitHub Student Developer Pack is approved
- [ ] `gh copilot` is installed and working
- [ ] VS Code is installed with recommended extensions

---

## 8. GitHub Codespaces — Your Cloud Backup Plan

If your local setup isn't cooperating on workshop day, **GitHub Codespaces** gives you a full development environment in your browser — no installation required.

### What is Codespaces?

It's VS Code running in the cloud, connected directly to a GitHub repo. You get a terminal, an editor, Git, Python — everything you need for the workshop. It starts in about 60 seconds.

### What does it cost?

**Free for verified students.** The Student Developer Pack includes:
- **180 core hours/month** (that's 90 hours on a 2-core machine — far more than you'll use)
- **20 GB storage/month**

If you're not a verified student, free GitHub accounts still get **120 core hours/month**.

### How to use it

1. Go to any GitHub repository (e.g., the workshop repo)
2. Click the green **Code** button
3. Click the **Codespaces** tab
4. Click **"Create codespace on main"**
5. Wait ~60 seconds for the environment to build
6. You'll see a full VS Code interface in your browser with a terminal at the bottom

That's it. Git is pre-installed, you're already authenticated, and you can push/pull directly.

### Try it now (optional)

Want to verify Codespaces works before the workshop?

1. Go to **https://github.com/johnazariah/git-and-github**
2. Click **Code → Codespaces → Create codespace on main**
3. Once it loads, open the terminal and run:
   ```bash
   git --version
   gh auth status
   ```
4. If both work, you have a working backup environment 🎉
5. **Stop the codespace when you're done** — go to https://github.com/codespaces, click the `...` menu next to it, and select "Stop codespace" (saves your free hours)

> **When to use Codespaces vs. local**: Local is better for day-to-day research work (faster, works offline). Codespaces is great as a backup, for quick experiments, and when you need a consistent environment across machines. Our research templates include devcontainer configurations that make Codespaces environments fully pre-configured automatically.

### Managing your Codespaces

- **Dashboard**: https://github.com/codespaces — see all your codespaces
- **Stop** a codespace when you're done to save hours (it auto-stops after 30 min of inactivity)
- **Delete** codespaces you no longer need to free up storage
- **Machine type**: The default 2-core machine is fine for everything in this workshop

---

## Troubleshooting

### Git issues

**"git: command not found"**
- Restart your terminal after installing Git
- macOS: try `xcode-select --install`
- Windows: make sure you're using Git Bash, not PowerShell

**"warning: LF will be replaced by CRLF"** (Windows)
- This is normal on Windows. To silence it:
  ```bash
  git config --global core.autocrlf true
  ```

### GitHub CLI issues

**"gh: command not found"**
- Restart your terminal after installing
- Windows: try installing from https://cli.github.com/ directly

**"error: authentication failed"**
- Run `gh auth login` again
- Make sure you authorize the CLI in your browser when prompted

**"could not determine base repo"**
- This is fine — it just means you're not inside a Git repo. You'll be once the workshop starts.

### SSH issues

**"Permission denied (publickey)"**
- Your SSH key isn't set up correctly
- Easiest fix: switch to the GitHub CLI method (step 4) instead of SSH
- Or check that your key is added: `ssh-add -l`

### GitHub Copilot issues

**"Your account does not have Copilot access"**
- Your Student Developer Pack may not be approved yet — check https://education.github.com/pack
- You can still do the whole workshop without Copilot — it's a bonus

**"gh: 'copilot' is not a known extension"**
- Run: `gh extension install github/gh-copilot`

### Codespaces issues

**"You've used all your included Codespaces hours"**
- This is unlikely (180 hours/month is a lot), but if it happens:
  - Delete unused codespaces at https://github.com/codespaces
  - Stop running codespaces you're not actively using
  - Switch to local setup for the workshop

**Codespace is slow or frozen**
- Try stopping and restarting it from https://github.com/codespaces
- Or create a new one (delete the old one first to free storage)

---

## Need Help?

If you're stuck on any step, don't worry:

1. **Come to the workshop 15 minutes early** — we'll help you get set up
2. **Email [INSTRUCTOR EMAIL]** with a screenshot of the error
3. **Worst case**: we'll get you into a GitHub Codespace during the workshop — you'll be up and running in 60 seconds

**The most important things are**: Git installed, GitHub account created, and authentication working. Everything else is a bonus.
