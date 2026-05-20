#!/usr/bin/env bash
#
# Copilot Demo Prep
# Run this before the workshop to stage the Copilot demo scenario.
#
# What it does:
#   1. Creates a temporary repo with a "large" data file committed
#   2. You use this repo on stage to ask Copilot:
#      "I accidentally committed a large data file. How do I remove it?"
#
# Usage:
#   cd ~/Desktop   # or wherever you want the demo repo
#   bash /path/to/git-and-github/instructor/copilot-demo-prep.sh
#
# Cleanup:
#   rm -rf copilot-demo
#
set -euo pipefail

DEMO_DIR="copilot-demo"

echo "=== Copilot Demo Prep ==="
echo ""

# Create a demo repo
if [ -d "$DEMO_DIR" ]; then
    echo "Directory '$DEMO_DIR' already exists. Remove it first:"
    echo "  rm -rf $DEMO_DIR"
    exit 1
fi

mkdir "$DEMO_DIR"
cd "$DEMO_DIR"
git init

# Create a simple analysis script
cat > analysis.py << 'PYTHON'
"""Quick analysis of experimental results."""
import pandas as pd

def summarise(filepath):
    df = pd.read_csv(filepath)
    print(f"Records: {len(df)}")
    print(df.describe())
    return df

if __name__ == "__main__":
    summarise("data/results.csv")
PYTHON

cat > README.md << 'MD'
# My Research Project
Analysing experimental results from the lab.
MD

git add .
git commit -m "Add analysis script and README"

# Now "accidentally" commit a large data file
mkdir -p data
echo "Generating a fake large data file..."
# Create a ~2MB CSV (small enough to commit but big enough to make the point)
python3 -c "
import random, csv, io
header = ['id','timestamp','temperature','pressure','humidity','sensor_id']
rows = []
for i in range(50000):
    rows.append([i, f'2026-01-{(i%28)+1:02d}T{i%24:02d}:00:00',
                 round(20 + random.gauss(0, 5), 2),
                 round(1013 + random.gauss(0, 10), 2),
                 round(60 + random.gauss(0, 15), 2),
                 f'sensor-{i%10:02d}'])
with open('data/results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
print(f'Created data/results.csv ({len(rows)} rows)')
"

git add data/results.csv
git commit -m "Add experimental data"

echo ""
echo "=== Demo repo ready ==="
echo ""
echo "The repo has 2 commits:"
git log --oneline
echo ""
echo "The 'mistake' is in the second commit: a 2MB CSV file."
echo ""
echo "During the demo, ask Copilot:"
echo ""
echo '  gh copilot suggest "I accidentally committed a large data file'
echo '  to my repo and pushed it. How do I remove it from the git'
echo '  history completely?"'
echo ""
echo "Or for the simpler demo:"
echo ""
echo '  gh copilot explain "git rebase -i HEAD~3"'
echo ""
echo "To clean up afterwards: rm -rf $(pwd)"
