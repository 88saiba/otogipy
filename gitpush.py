import subprocess
import os

# Configuration - Replace with your GitHub credentials
USERNAME = "<YOUR_USERNAME>"
TOKEN = "<YOUR_PERSONAL_ACCESS_TOKEN>"
REPO_URL = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/<YOUR_REPOSITORY>.git"
CREDENTIALS_FILE = os.path.expanduser("~/.git-credentials")

def run_command(command):
    """Execute shell command and return the output"""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result.stdout

def setup_git_credentials():
    """Set up Git credentials file if not already present"""
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'w') as file:
            file.write(f"https://{USERNAME}:{TOKEN}@github.com\n")

def git_push(commit_message):
    """Add files, commit, and push to GitHub"""
    # Set up Git credentials
    setup_git_credentials()
    
    # Add files and commit
    run_command("git add .")
    run_command(f"git commit -m \"{commit_message}\"")
    
    # Set remote URL and push
    run_command(f"git remote set-url origin {REPO_URL}")
    run_command("git push origin main")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gitpush.py <commit_message>")
        print("Example: python gitpush.py 'Your commit message'")
        sys.exit(1)
    
    commit_message = sys.argv[1]
    git_push(commit_message)
