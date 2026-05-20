# Git & GitHub for Research Collaboration

A **2-hour hands-on workshop** for STEM graduate students who want to use Git and GitHub effectively in their research.

Whether you're managing analysis scripts, collaborating on code with your lab group, or preparing to publish reproducible research — this workshop will give you the practical skills to get started.

## 🎯 What You'll Learn

- **Why version control matters** for reproducibility and collaboration in research
- **Core Git workflow** — commits, diffs, history, and `.gitignore`
- **GitHub as a research tool** — repositories, Issues, Pull Requests, and GitHub Pages
- **Collaborative workflows** — branching, merging, and resolving conflicts as a team
- **Research patterns** — tagging submissions, DOIs with Zenodo, managing notebooks

## 📋 Before the Workshop

**👉 [Complete the setup guide](pre-workshop/setup-guide.md) before you arrive.**

You'll need Git installed, a GitHub account, and authentication configured. The guide takes about 15–20 minutes. If you get stuck, arrive 15 minutes early and we'll help.

## 🗂️ Workshop Materials

| Material | Description |
|----------|-------------|
| [Pre-Workshop Setup](pre-workshop/setup-guide.md) | Install Git, create GitHub account, configure auth |
| [Exercise 1: Solo Repository](exercises/exercise-1-solo-repo.md) | Create your first research repo with meaningful commits |
| [Exercise 2: Collaboration](exercises/exercise-2-collaboration.md) | Paired exercise — branches, PRs, and merge conflicts |
| [Template Repo Files](exercises/template-repo/) | Starter files for the collaboration exercise |
| [Git Cheat Sheet](handouts/git-cheatsheet.md) | Command reference + research-specific patterns |
| [GitHub Copilot One-Pager](handouts/copilot-one-pager.md) | AI-assisted Git help — setup and example prompts |

## 📚 Resources

### Books & Tutorials

- **[Pro Git](https://git-scm.com/book/en/v2)** — The definitive Git book. Free online. Chapters 1–3 cover everything in this workshop and more.
- **[GitHub Skills](https://skills.github.com/)** — Interactive, hands-on courses that run directly in GitHub repositories. Start with *Introduction to GitHub*.
- **[Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/)** — Excellent lesson designed specifically for researchers. Covers similar ground to our workshop.
- **[The Turing Way](https://book.the-turing-way.org/reproducible-research/vcs)** — A guide to reproducible data science. The version control chapter explains why and how researchers should use Git.
- **[Happy Git and GitHub for the useR](https://happygitwithr.com/)** — If you use R, this is the best guide for integrating Git into your R workflow.

### Git + Notebooks

- **[nbstripout](https://github.com/kynan/nbstripout)** — Automatically strip notebook outputs before committing. Keeps diffs clean.
- **[Jupytext](https://jupytext.readthedocs.io/)** — Sync Jupyter notebooks with plain-text `.py` or `.md` files for version-friendly diffs.
- **[nbdime](https://nbdime.readthedocs.io/)** — Diff and merge tools built specifically for Jupyter notebooks.
- **[ReviewNB](https://www.reviewnb.com/)** — Visual diff and commenting for notebooks in GitHub Pull Requests.

### Research-Specific

- **[GitHub + Zenodo Integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)** — Get a DOI for your code repository so it can be cited like a paper.
- **[Choose a License](https://choosealicense.com/)** — Simple guide to picking an open-source license for your research code.
- **[FAIR Principles for Research Software](https://www.nature.com/articles/s41597-022-01710-x)** — Why making your code Findable, Accessible, Interoperable, and Reusable matters.
- **[The Journal of Open Source Software (JOSS)](https://joss.theoj.org/)** — Publish your research software as a citable paper. Requires a GitHub repo.

### Cheat Sheets & Quick References

- **[GitHub Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)** — Official two-page reference from GitHub Education
- **[Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html)** — Visual explanations of how Git commands work
- **[Oh Shit, Git!?!](https://ohshitgit.com/)** — Plain-English solutions for common Git mistakes (language warning 😄)
- **[Git Flight Rules](https://github.com/k88hudson/git-flight-rules)** — A comprehensive FAQ for Git problems, inspired by NASA flight rules

### GitHub Features for Research Teams

- **[GitHub Pages](https://pages.github.com/)** — Publish project documentation as a website directly from your repo
- **[GitHub Actions](https://docs.github.com/en/actions)** — Automate testing, data validation, and deployments on every push
- **[GitHub Organizations](https://docs.github.com/en/organizations)** — Create a shared space for your lab group with managed permissions
- **[GitHub Discussions](https://docs.github.com/en/discussions)** — Forum-style conversations for your project (good for research Q&A)

## ⏱️ Workshop Schedule

| Block | Topic | Duration |
|-------|-------|----------|
| 1 | Why Version Control Matters for Research | 10 min |
| 2 | Git Fundamentals — Solo Workflow | 30 min |
| 3 | GitHub — Your Research Portfolio + Pages | 20 min |
| 4 | Branching & Collaboration ⭐ | 40 min |
| 5 | Research Workflow Patterns | 5 min |
| 6 | GitHub Copilot Demo & Wrap-up | 10 min |
|   | *Buffer for troubleshooting* | *~5 min* |

## 🤝 Contributing

Found a typo? Have a suggestion? [Open an issue](../../issues) or submit a pull request — that's what this workshop is all about!

## 📄 License

This workshop is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to reuse, adapt, and share with attribution.
