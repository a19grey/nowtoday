#!/bin/bash

# Function to print error messages
error() {
    echo "ERROR: $1" >&2
    exit 1
}

# Check if GIT_REPLIT_PERSONAL_TOKEN is set
if [ -z "$GIT_REPLIT_PERSONAL_TOKEN" ]; then
    error "GIT_REPLIT_PERSONAL_TOKEN is not set. Please set it with your GitHub Personal Access Token."
fi

# Set Git user name
git config --global user.name "a19grey" || error "Failed to set Git user name"

# Set Git user email
git config --global user.email "a19grey@gmail.com" || error "Failed to set Git user email"

# Set credential helper to store credentials
git config --global credential.helper store || error "Failed to set credential helper"

# Set up HTTPS instead of SSH
git config --global url."https://github.com/".insteadOf "git@github.com:" || error "Failed to set HTTPS as default"

# Store the GitHub token
echo "https://a19grey:$GIT_REPLIT_PERSONAL_TOKEN@github.com" > ~/.git-credentials
chmod 600 ~/.git-credentials || error "Failed to set permissions for git credentials file"

echo "Git configuration has been set up successfully:"
echo "Name: $(git config --global user.name)"
echo "Email: $(git config --global user.email)"
echo "Credential helper: $(git config --global credential.helper)"
echo "GitHub token has been stored in ~/.git-credentials"

# Display remote repository information if available
if git remote -v &>/dev/null; then
    git remote -v
else
    echo "No Git remote configured in this directory"
fi

# Test GitHub authentication
if curl -s -H "Authorization: token $GIT_REPLIT_PERSONAL_TOKEN" https://api.github.com/user | grep -q "login"; then
    echo "GitHub authentication successful"
else
    error "GitHub authentication failed. Please check your token."
fi

echo "Git setup completed successfully. You can now use Git with your GitHub token."

# Run the app
echo "Running the app now with npm run dev & python app.py"
npm run dev & python app.py
