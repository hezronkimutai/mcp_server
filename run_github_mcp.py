#!/usr/bin/env python3
"""
Simple GitHub MCP Runner - Downloads and runs the MCP server from GitHub
This works without requiring uvx or complex setup.
"""

import os
import sys
import tempfile
import urllib.request
import subprocess
from pathlib import Path

def main():
    """Download and run the MCP server from GitHub"""
    
    # GitHub raw URLs
    script_url = "https://raw.githubusercontent.com/hezronkimutai/mcp_server/main/advanced_mcp_server.py"
    requirements_url = "https://raw.githubusercontent.com/hezronkimutai/mcp_server/main/requirements.txt"
    
    try:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Download the main script
            script_path = temp_path / "advanced_mcp_server.py"
            print(f"Downloading MCP server from GitHub...", file=sys.stderr)
            urllib.request.urlretrieve(script_url, script_path)
            
            # Download and install requirements
            requirements_path = temp_path / "requirements.txt"
            try:
                urllib.request.urlretrieve(requirements_url, requirements_path)
                print("Installing requirements...", file=sys.stderr)
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", "-r", str(requirements_path), "--quiet", "--user"
                ])
            except Exception as e:
                print(f"Warning: Could not install requirements: {e}", file=sys.stderr)
            
            # Change to temp directory and run the script
            os.chdir(temp_dir)
            
            # Run the downloaded script
            subprocess.run([sys.executable, str(script_path)])
            
    except Exception as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()