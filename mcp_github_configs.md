# MCP GitHub Configuration Options

Here are different ways to configure your MCP server to run directly from GitHub:

## Option 1: Using uvx with Git Repository (Recommended)

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
      "env": {
        "PYTHONPATH": "."
      },
      "disabled": false,
      "autoApprove": [
        "scrape_website", 
        "analyze_data", 
        "system_monitor",
        "file_operations",
        "api_integration", 
        "database_query",
        "generate_report"
      ]
    }
  }
}
```

## Option 2: Using Python with Direct GitHub Raw URL

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["-c", "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/hezronkimutai/mcp_server/main/advanced_mcp_server.py').read())"],
      "disabled": false,
      "autoApprove": [
        "scrape_website", 
        "analyze_data", 
        "system_monitor",
        "file_operations",
        "api_integration", 
        "database_query",
        "generate_report"
      ]
    }
  }
}
```

## Option 3: Using a Wrapper Script that Downloads from GitHub

Create a local wrapper script that downloads and runs the latest version:

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["github_mcp_runner.py"],
      "disabled": false,
      "autoApprove": [
        "scrape_website", 
        "analyze_data", 
        "system_monitor",
        "file_operations",
        "api_integration", 
        "database_query",
        "generate_report"
      ]
    }
  }
}
```

## Option 4: Using pip install from GitHub

If you structure it as a proper Python package:

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["git+https://github.com/hezronkimutai/mcp_server.git"],
      "disabled": false,
      "autoApprove": [
        "scrape_website", 
        "analyze_data", 
        "system_monitor",
        "file_operations",
        "api_integration", 
        "database_query",
        "generate_report"
      ]
    }
  }
}
```

## Benefits of GitHub-based Configuration:

1. **Always Latest Version**: Automatically uses the most recent code
2. **No Local Storage**: Doesn't clutter your local filesystem
3. **Easy Updates**: Just push to GitHub and restart MCP server
4. **Shareable**: Others can use the same configuration
5. **Version Control**: Full git history and rollback capabilities

## Prerequisites:

- **For uvx method**: Install uv/uvx (`pip install uv`)
- **For git method**: Git must be installed and accessible
- **For all methods**: Python and pip must be available

## Recommended Approach:

**Option 1 (uvx with git)** is the most robust because:
- Handles dependencies automatically
- Creates isolated environment
- Works reliably across different systems
- Supports proper Python package structure

The repository is now live at: https://github.com/hezronkimutai/mcp_server