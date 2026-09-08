#!/bin/bash
# -------------------------------------------------------------
# Quick Deploy Script for Vivek Sabale's Academic Website
# Usage:
#   ./deploy.sh "Your commit message here"
#   or simply: ./deploy.sh
# -------------------------------------------------------------

set -e

# Default commit message if none provided
COMMIT_MSG="${1:-Update website content}"

echo "🚀 Staging changes..."
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "ℹ️ No changes detected to commit."
    exit 0
fi

echo "📝 Committing: '$COMMIT_MSG'..."
git commit -m "$COMMIT_MSG"

echo "⬆️ Pushing to GitHub (main branch)..."
git push origin main

echo ""
echo "✅ Changes pushed successfully!"
echo "⚙️ GitHub Actions is now automatically building and deploying your site."
echo "🌐 Live site will update in ~1-2 minutes at: https://viveksabale1998.github.io/"
