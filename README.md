# Advanced MCP Server

A comprehensive Model Context Protocol (MCP) server that provides advanced capabilities for web scraping, data analysis, system monitoring, file operations, API integrations, and report generation.

## Features

### 🌐 Web Scraping
- Advanced HTML parsing with BeautifulSoup
- Extract links, images, and clean text content
- Automatic database storage of scraped content
- Content analysis and statistics

### 📊 Data Analysis
- CSV file analysis with pandas
- Statistical summaries and correlations
- Distribution analysis and trend detection
- Automatic visualization generation with matplotlib/seaborn

### 🖥️ System Monitoring
- Real-time CPU, memory, and disk usage tracking
- Configurable monitoring duration and intervals
- Historical data storage and analysis
- Performance trend visualization

### 📁 File Operations
- Advanced file and directory search
- Content analysis and statistics
- Automated backup creation
- Cleanup operations for temporary files
- File comparison capabilities

### 🔌 API Integration
- HTTP requests with full method support
- Intelligent caching system
- Error handling and retry logic
- Response parsing and validation

### 🗄️ Database Operations
- Built-in SQLite database for data persistence
- Custom SQL query execution
- Data export and analysis capabilities
- Automatic schema management

### 📋 Report Generation
- System health reports with recommendations
- Web scraping analysis summaries
- Data summary reports
- Multiple output formats (Markdown, JSON, HTML)
- Integrated charts and visualizations

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make the server executable:
```bash
chmod +x advanced_mcp_server.py
```

## MCP Configuration

## Quick Start - Run from GitHub

The easiest way to use this server is to run it directly from GitHub:

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
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

## Local Installation

If you prefer to run locally:

1. Clone the repository:
```bash
git clone https://github.com/hezronkimutai/mcp_server.git
cd mcp_server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add to your MCP configuration:
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["path/to/mcp_server/advanced_mcp_server.py"],
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

## Available Tools

### scrape_website
Scrape and analyze website content with advanced parsing capabilities.

**Parameters:**
- `url` (required): URL to scrape
- `extract_links` (optional): Extract all links from the page
- `extract_images` (optional): Extract all images from the page  
- `save_to_db` (optional): Save content to database

**Example:**
```json
{
  "url": "https://example.com",
  "extract_links": true,
  "extract_images": true,
  "save_to_db": true
}
```

### analyze_data
Perform statistical analysis on CSV data with visualizations.

**Parameters:**
- `file_path` (required): Path to CSV file
- `analysis_type` (required): Type of analysis ("summary", "correlation", "distribution", "trends")
- `create_visualization` (optional): Generate charts and graphs

**Example:**
```json
{
  "file_path": "data.csv",
  "analysis_type": "correlation",
  "create_visualization": true
}
```

### system_monitor
Monitor system resources and performance metrics.

**Parameters:**
- `duration_minutes` (optional): How long to monitor (default: 1)
- `interval_seconds` (optional): Sampling interval (default: 10)
- `save_metrics` (optional): Save to database (default: true)

**Example:**
```json
{
  "duration_minutes": 5,
  "interval_seconds": 30,
  "save_metrics": true
}
```

### file_operations
Advanced file system operations with search and analysis.

**Parameters:**
- `operation` (required): Operation type ("search", "analyze", "backup", "cleanup", "compare")
- `path` (required): File or directory path
- `pattern` (optional): Search pattern for search operations
- `options` (optional): Additional operation-specific options

**Example:**
```json
{
  "operation": "search",
  "path": "/project/src",
  "pattern": "TODO",
  "options": {}
}
```

### api_integration
Make API calls with caching and error handling.

**Parameters:**
- `endpoint` (required): API endpoint URL
- `method` (optional): HTTP method (default: "GET")
- `headers` (optional): Request headers
- `data` (optional): Request body data
- `use_cache` (optional): Enable caching (default: true)
- `cache_duration_hours` (optional): Cache duration (default: 1)

**Example:**
```json
{
  "endpoint": "https://api.example.com/data",
  "method": "GET",
  "headers": {"Authorization": "Bearer token"},
  "use_cache": true,
  "cache_duration_hours": 2
}
```

### database_query
Execute SQL queries on the internal database.

**Parameters:**
- `query` (required): SQL query to execute
- `table` (optional): Target table name
- `limit` (optional): Result limit (default: 100)

**Example:**
```json
{
  "query": "SELECT * FROM web_scrapes WHERE title LIKE '%python%'",
  "limit": 50
}
```

### generate_report
Generate comprehensive reports from collected data.

**Parameters:**
- `report_type` (required): Report type ("system_health", "web_analysis", "data_summary")
- `format` (optional): Output format ("markdown", "json", "html")
- `include_charts` (optional): Include visualizations (default: true)

**Example:**
```json
{
  "report_type": "system_health",
  "format": "markdown",
  "include_charts": true
}
```

## Database Schema

The server automatically creates and manages an SQLite database with the following tables:

### web_scrapes
- `id`: Primary key
- `url`: Scraped URL
- `title`: Page title
- `content`: Extracted text content
- `scraped_at`: Timestamp

### system_metrics
- `id`: Primary key
- `cpu_percent`: CPU usage percentage
- `memory_percent`: Memory usage percentage
- `disk_usage`: Disk usage percentage
- `recorded_at`: Timestamp

### api_cache
- `id`: Primary key
- `endpoint`: API endpoint URL
- `response_data`: Cached response
- `cached_at`: Cache timestamp

## Error Handling

The server includes comprehensive error handling:
- Network timeouts and connection errors
- File system permission issues
- Database connection problems
- Invalid data format handling
- Resource cleanup on failures

## Performance Considerations

- Database operations are optimized with proper indexing
- Large datasets are processed in chunks
- Memory usage is monitored and controlled
- Caching reduces redundant API calls
- Visualizations are generated efficiently

## Security Features

- Input validation and sanitization
- SQL injection prevention
- File system access controls
- Safe temporary file handling
- Error message sanitization

## Contributing

This server is designed to be extensible. You can add new tools by:

1. Adding the tool definition to `handle_list_tools()`
2. Implementing the tool handler in `handle_call_tool()`
3. Creating the corresponding method in the class
4. Updating the documentation

## GitHub Configuration Options

This repository provides multiple ways to run the MCP server directly from GitHub:

### Option 1: uvx with Git (Recommended)
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
      "disabled": false
    }
  }
}
```

### Option 2: Direct Python Execution
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["-c", "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/hezronkimutai/mcp_server/main/advanced_mcp_server.py').read())"],
      "disabled": false
    }
  }
}
```

### Option 3: Using Wrapper Script
Download `github_mcp_runner.py` and use:
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["github_mcp_runner.py"],
      "disabled": false
    }
  }
}
```

## Repository Structure

```
mcp_server/
├── advanced_mcp_server.py      # Main MCP server
├── requirements.txt            # Python dependencies
├── setup.py                   # Package setup
├── github_mcp_runner.py       # GitHub wrapper script
├── mcp_config_*.json          # Ready-to-use configurations
├── mcp_github_configs.md      # Detailed configuration guide
└── README.md                  # This file
```

## License

This project is open source and available under the MIT License.