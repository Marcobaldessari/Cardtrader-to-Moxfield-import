#!/bin/bash

# Setup script for Cardtrader to Moxfield converter repository

echo "Setting up Git repository for Cardtrader to Moxfield converter..."

# Initialize git repository (if not already done)
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
else
    echo "Git repository already initialized."
fi

# Add all files (respecting .gitignore)
echo "Adding files to git..."
git add .

# Check what files will be committed
echo "Files to be committed:"
git status --porcelain

# Make initial commit
echo "Making initial commit..."
git commit -m "Initial commit: Cardtrader to Moxfield CSV converter

- Python script to convert Cardtrader XLS files to Moxfield CSV format
- Proper field mappings for condition, language, and foil
- Comprehensive documentation and requirements
- Handles multiple XLS files and provides conversion statistics"

echo ""
echo "✓ Git repository setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote origin: git remote add origin <your-github-repo-url>"
echo "3. Push to GitHub: git push -u origin main"
echo ""
echo "Note: The .gitignore file will exclude:"
echo "- Python cache files (__pycache__, *.pyc)"
echo "- System files (.DS_Store, Thumbs.db)"
echo "- IDE files (.vscode, .idea)"
echo "- Virtual environments"
echo "- Log files"
