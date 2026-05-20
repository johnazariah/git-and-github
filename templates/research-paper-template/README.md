# Research Paper Template

A Git-friendly template for writing academic papers in LaTeX with **automatic PDF builds** via GitHub Actions.

## ✨ What This Does

- **Push LaTeX → get a PDF.** Every commit to `paper/` triggers a GitHub Action that compiles your paper and makes the PDF available.
- **Release your paper** → the compiled PDF is automatically attached to the GitHub Release (ready for Zenodo DOI minting).
- **Devcontainer included** → open in GitHub Codespaces or VS Code and start writing immediately. No local LaTeX installation needed.

## 📁 Structure

```
├── paper/
│   ├── main.tex          ← Your paper (start here)
│   └── references.bib    ← BibTeX references
├── figures/               ← Figures (PDF/PNG/SVG)
├── .devcontainer/         ← Codespaces / VS Code dev environment
└── .github/workflows/
    ├── build-paper.yml    ← Builds PDF on every push
    └── release-paper.yml  ← Attaches PDF to GitHub Releases
```

## 🚀 Getting Started

### Option 1: GitHub Codespaces (no setup)
1. Click **Code → Codespaces → New codespace**
2. Wait for the environment to build (~2 min first time)
3. Open `paper/main.tex` and start writing
4. PDF builds automatically on save (via LaTeX Workshop extension)

### Option 2: Local
1. Fork or use this template
2. Install a LaTeX distribution ([TeX Live](https://tug.org/texlive/) or [MiKTeX](https://miktex.org/))
3. Edit `paper/main.tex`
4. Build: `cd paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`

### Option 3: Just push and let GitHub build it
1. Edit files directly on GitHub or locally
2. Push to `main`
3. Go to **Actions** tab → download the PDF artifact

## 📄 Publishing a Version

When you're ready to submit:

```bash
git tag -a v1.0-submitted -m "Submitted to Journal of Example Studies"
git push origin --tags
```

Then create a **Release** on GitHub from that tag. The workflow will automatically attach the compiled PDF.

### Getting a DOI via Zenodo
1. Go to [zenodo.org](https://zenodo.org) and link your GitHub repo
2. Create a Release on GitHub
3. Zenodo archives it and mints a DOI
4. Add the DOI badge to this README

## 🤝 Collaborating

1. Create a branch for your changes: `git checkout -b revisions/reviewer-1`
2. Make your edits to `paper/main.tex`
3. Push and open a Pull Request
4. The PR will show a diff of your LaTeX changes
5. The PDF builds automatically so reviewers can download and check the compiled output

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
