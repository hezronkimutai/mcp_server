#!/usr/bin/env python3
"""
GitHub MCP Runner - Downloads and runs the latest MCP server from GitHub
This ensures you always have the latest version without manual updates.
"""

import os
import sys
import tempfile
import urllib.request
import subprocess
from pathlib import Path

# Configuration
GITHUB_USER = "YOUR_USERNAME"  # Replace with your GitHub username
REPO_NAME = "advanced-mcp-server"
BRANCH = "main"
SCRIPT_NAME = "advanced_mcp_server.py"
REQUIREMENTS_NAME = "requirements.txt"

# URLs
SCRIPT_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{SCRIPT_NAME}"
REQUIREMENTS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{REQUIREMENTS_NAME}"

def download_file(url, local_path):
    """Download a file from URL to local path"""
    try:
        urllib.request.urlretrieve(url, local_path)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False

def install_requirements(requirements_path):
    """Install requirements from requirements.txt"""
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", requirements_path, "--quiet"
        ])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}", file=sys.stderr)
        return False

def main():
    """Main function to download and run the MCP server"""
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Download the main script
        script_path = temp_path / SCRIPT_NAME
        print(f"Downloading {SCRIPT_NAME} from GitHub...", file=sys.stderr)
        if not download_file(SCRIPT_URL, script_path):
            sys.exit(1)
        
        # Download requirements
        requirements_path = temp_path / REQUIREMENTS_NAME
        print(f"Downloading {REQUIREMENTS_NAME} from GitHub...", file=sys.stderr)
        if download_file(REQUIREMENTS_URL, requirements_path):
            print("Installing requirements...", file=sys.stderr)
            install_requirements(requirements_path)
        
        # Make script executable and run it
        os.chmod(script_path, 0o755)
        
        # Change to temp directory and run the script
        os.chdir(temp_dir)
        
        # Import and run the downloaded script
        sys.path.insert(0, str(temp_path))
        
        try:
            # Execute the downloaded script
            with open(script_path, 'r') as f:
                script_content = f.read()
            
            # Execute in the current namespace
            exec(script_content)
            
        except Exception as e:
            print(f"Error running MCP server: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()