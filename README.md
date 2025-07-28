# Advanced MCP Server

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![GitHub Stars](https://img.shields.io/github/stars/hezronkimutai/mcp_server?style=social)](https://github.com/hezronkimutai/mcp_server)

A comprehensive Model Context Protocol (MCP) server that provides advanced capabilities for web scraping, data analysis, system monitoring, file operations, API integrations, and report generation. Built with Python and designed for seamless integration with MCP-compatible clients like Claude Desktop.

## 🚀 Quick Start

The fastest way to get started is using the GitHub-hosted version:

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
      "disabled": false,
      "autoApprove": ["scrape_website", "analyze_data", "system_monitor", "file_operations", "api_integration", "database_query", "generate_report"]
    }
  }
}
```

Add this configuration to your MCP client (e.g., Claude Desktop) and start using the server immediately!

## ✨ Key Features

### 🌐 Web Scraping & Content Analysis
- **Advanced HTML parsing** with BeautifulSoup4
- **Smart content extraction** - links, images, and clean text
- **Automatic data persistence** in SQLite database
- **Content analytics** and comprehensive statistics
- **Duplicate detection** and content deduplication

### 📊 Data Analysis & Visualization
- **CSV file analysis** with pandas integration
- **Statistical insights** - summaries, correlations, distributions
- **Trend detection** and pattern analysis
- **Professional visualizations** with matplotlib and seaborn
- **Export capabilities** in multiple formats

### 🖥️ System Monitoring & Performance
- **Real-time monitoring** of CPU, memory, and disk usage
- **Configurable intervals** and monitoring duration
- **Historical data tracking** with trend analysis
- **Performance alerts** and threshold monitoring
- **Resource optimization** recommendations

### 📁 Advanced File Operations
- **Intelligent file search** with pattern matching
- **Content analysis** and metadata extraction
- **Automated backup** creation and management
- **Cleanup operations** for temporary and cache files
- **File comparison** and diff analysis
- **Batch operations** support

### 🔌 API Integration & Caching
- **Full HTTP method support** (GET, POST, PUT, DELETE, etc.)
- **Intelligent caching system** with configurable TTL
- **Automatic retry logic** with exponential backoff
- **Response validation** and error handling
- **Rate limiting** and request throttling

### 🗄️ Database Operations & Management
- **Built-in SQLite database** for data persistence
- **Custom SQL query execution** with safety checks
- **Data export utilities** (CSV, JSON, XML)
- **Schema management** and migrations
- **Query optimization** and performance monitoring

### 📋 Comprehensive Report Generation
- **System health reports** with actionable recommendations
- **Web scraping analytics** and content summaries
- **Data analysis reports** with statistical insights
- **Multiple output formats** (Markdown, JSON, HTML, PDF)
- **Integrated charts** and interactive visualizations
- **Automated scheduling** and delivery options

## 📦 Installation

### Prerequisites
- **Python 3.8+** (recommended: Python 3.11+)
- **pip** package manager
- **Git** (for GitHub installation)

### Method 1: Direct GitHub Installation (Recommended)

No local setup required! The server runs directly from GitHub:

```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
      "disabled": false,
      "autoApprove": ["scrape_website", "analyze_data", "system_monitor", "file_operations", "api_integration", "database_query", "generate_report"]
    }
  }
}
```

### Method 2: Local Installation

For development or customization:

1. **Clone the repository:**
```bash
git clone https://github.com/hezronkimutai/mcp_server.git
cd mcp_server
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Make executable (Unix/Linux/macOS):**
```bash
chmod +x advanced_mcp_server.py
```

4. **Add to MCP configuration:**
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "python",
      "args": ["C:/path/to/mcp_server/advanced_mcp_server.py"],
      "disabled": false,
      "autoApprove": ["scrape_website", "analyze_data", "system_monitor", "file_operations", "api_integration", "database_query", "generate_report"]
    }
  }
}
```

### Method 3: Package Installation

Install as a Python package:

```bash
pip install git+https://github.com/hezronkimutai/mcp_server.git
```

Then use in your MCP configuration:
```json
{
  "mcpServers": {
    "advanced-server": {
      "command": "advanced-mcp-server",
      "disabled": false,
      "autoApprove": ["scrape_website", "analyze_data", "system_monitor", "file_operations", "api_integration", "database_query", "generate_report"]
    }
  }
}
```
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

## 🛠️ Available Tools

### 🌐 scrape_website
Advanced web scraping with content analysis and database storage.

**Parameters:**
- `url` (required): Target URL to scrape
- `extract_links` (optional, default: false): Extract all hyperlinks
- `extract_images` (optional, default: false): Extract image URLs and metadata  
- `save_to_db` (optional, default: true): Persist content to database

**Real-world Examples:**
```json
// Basic website scraping
{
  "url": "https://example.com"
}

// Complete content extraction with database storage
{
  "url": "https://news.ycombinator.com",
  "extract_links": true,
  "extract_images": true,
  "save_to_db": true
}

// Blog post analysis
{
  "url": "https://blog.example.com/post/123",
  "extract_links": false,
  "extract_images": false,
  "save_to_db": true
}
```

### 📊 analyze_data
Comprehensive statistical analysis with professional visualizations.

**Parameters:**
- `file_path` (required): Path to CSV file
- `analysis_type` (required): Analysis type - "summary", "correlation", "distribution", "trends", "outliers"
- `create_visualization` (optional, default: true): Generate charts and graphs
- `columns` (optional): Specific columns to analyze
- `save_results` (optional, default: true): Save analysis to database

**Real-world Examples:**
```json
// Sales data analysis with trends
{
  "file_path": "/data/sales_2024.csv",
  "analysis_type": "trends",
  "create_visualization": true,
  "columns": ["revenue", "units_sold", "date"]
}

// Customer data correlation analysis
{
  "file_path": "/data/customers.csv",
  "analysis_type": "correlation",
  "create_visualization": true,
  "save_results": true
}

// Quick statistical summary
{
  "file_path": "/logs/performance_metrics.csv",
  "analysis_type": "summary",
  "create_visualization": false
}
```

### 🖥️ system_monitor
Real-time system performance monitoring with alerting.

**Parameters:**
- `duration_minutes` (optional, default: 1): Monitoring duration
- `interval_seconds` (optional, default: 10): Data collection interval
- `save_metrics` (optional, default: true): Store metrics in database
- `alert_thresholds` (optional): CPU/Memory/Disk usage alert levels
- `generate_report` (optional, default: false): Create performance report

**Real-world Examples:**
```json
// Quick system health check
{
  "duration_minutes": 2,
  "interval_seconds": 5,
  "save_metrics": true
}

// Extended monitoring with alerts
{
  "duration_minutes": 30,
  "interval_seconds": 60,
  "save_metrics": true,
  "alert_thresholds": {"cpu": 80, "memory": 90, "disk": 85},
  "generate_report": true
}

// Lightweight monitoring for scripts
{
  "duration_minutes": 1,
  "interval_seconds": 30,
  "save_metrics": false
}
```

### 📁 file_operations
Advanced file system operations with intelligent search and analysis.

**Parameters:**
- `operation` (required): Operation type - "search", "analyze", "backup", "cleanup", "compare", "organize"
- `path` (required): Target file or directory path
- `pattern` (optional): Search pattern (supports regex and glob)
- `options` (optional): Operation-specific configuration
- `recursive` (optional, default: true): Include subdirectories
- `file_types` (optional): Filter by file extensions

**Real-world Examples:**
```json
// Find TODO comments in project
{
  "operation": "search",
  "path": "/project/src",
  "pattern": "TODO|FIXME|HACK",
  "options": {"case_sensitive": false, "context_lines": 2},
  "recursive": true,
  "file_types": [".py", ".js", ".ts"]
}

// Analyze project structure
{
  "operation": "analyze",
  "path": "/project",
  "options": {"include_stats": true, "generate_tree": true},
  "recursive": true
}

// Clean temporary files
{
  "operation": "cleanup",
  "path": "/project",
  "pattern": "*.tmp|*.cache|__pycache__",
  "options": {"dry_run": false, "backup_before_delete": true}
}

// Backup important directories
{
  "operation": "backup",
  "path": "/important/data",
  "options": {"destination": "/backups", "compression": "gzip", "exclude_patterns": ["*.log", "*.tmp"]}
}
```

### 🔌 api_integration
Robust API integration with intelligent caching and error handling.

**Parameters:**
- `endpoint` (required): API endpoint URL
- `method` (optional, default: "GET"): HTTP method
- `headers` (optional): Request headers dictionary
- `data` (optional): Request body (JSON, form data, or raw)
- `params` (optional): URL query parameters
- `use_cache` (optional, default: true): Enable response caching
- `cache_duration_hours` (optional, default: 1): Cache TTL
- `timeout_seconds` (optional, default: 30): Request timeout
- `retry_attempts` (optional, default: 3): Number of retry attempts

**Real-world Examples:**
```json
// Fetch weather data with caching
{
  "endpoint": "https://api.openweathermap.org/data/2.5/weather",
  "method": "GET",
  "params": {"q": "London", "appid": "your_api_key"},
  "use_cache": true,
  "cache_duration_hours": 1
}

// Post data to API with retry logic
{
  "endpoint": "https://api.example.com/users",
  "method": "POST",
  "headers": {"Content-Type": "application/json", "Authorization": "Bearer token"},
  "data": {"name": "John Doe", "email": "john@example.com"},
  "use_cache": false,
  "retry_attempts": 5,
  "timeout_seconds": 60
}

// GraphQL query
{
  "endpoint": "https://api.github.com/graphql",
  "method": "POST",
  "headers": {"Authorization": "Bearer github_token"},
  "data": {"query": "query { viewer { login } }"},
  "use_cache": true,
  "cache_duration_hours": 24
}
```

### 🗄️ database_query
Execute SQL queries with safety checks and result formatting.

**Parameters:**
- `query` (required): SQL query to execute
- `table` (optional): Target table for simple operations
- `limit` (optional, default: 100): Maximum number of results
- `format` (optional, default: "json"): Output format - "json", "csv", "html"
- `parameters` (optional): Query parameters for prepared statements
- `export_file` (optional): Save results to file

**Real-world Examples:**
```json
// Analyze scraped content
{
  "query": "SELECT url, title, LENGTH(content) as content_length FROM web_scrapes WHERE scraped_at > datetime('now', '-7 days') ORDER BY scraped_at DESC",
  "limit": 50,
  "format": "json"
}

// System performance trends
{
  "query": "SELECT DATE(recorded_at) as date, AVG(cpu_percent) as avg_cpu, MAX(memory_percent) as max_memory FROM system_metrics WHERE recorded_at > datetime('now', '-30 days') GROUP BY DATE(recorded_at)",
  "format": "csv",
  "export_file": "/reports/performance_trends.csv"
}

// Search cached API responses
{
  "query": "SELECT endpoint, COUNT(*) as request_count, AVG(LENGTH(response_data)) as avg_response_size FROM api_cache GROUP BY endpoint",
  "limit": 20
}
```

### 📋 generate_report
Create comprehensive reports with visualizations and insights.

**Parameters:**
- `report_type` (required): Report type - "system_health", "web_analysis", "data_summary", "api_usage", "custom"
- `format` (optional, default: "markdown"): Output format - "markdown", "json", "html", "pdf"
- `include_charts` (optional, default: true): Generate visualizations
- `time_range` (optional): Data time range filter
- `save_to_file` (optional): Save report to specified file
- `email_recipients` (optional): Email addresses for report delivery
- `template` (optional): Custom report template

**Real-world Examples:**
```json
// Weekly system health report
{
  "report_type": "system_health",
  "format": "html",
  "include_charts": true,
  "time_range": "7_days",
  "save_to_file": "/reports/weekly_health_report.html"
}

// Web scraping analytics
{
  "report_type": "web_analysis",
  "format": "markdown",
  "include_charts": true,
  "time_range": "30_days",
  "save_to_file": "/reports/scraping_summary.md"
}

// Custom business intelligence report
{
  "report_type": "custom",
  "format": "pdf",
  "include_charts": true,
  "template": "business_dashboard",
  "save_to_file": "/reports/monthly_bi_report.pdf",
  "email_recipients": ["manager@company.com", "analyst@company.com"]
}
```

## 🗄️ Database Schema

The server automatically creates and manages an SQLite database with optimized tables:

### 📊 web_scrapes
Stores web scraping results with full-text search capabilities.
- `id`: Primary key (INTEGER)
- `url`: Scraped URL (TEXT, INDEXED)
- `title`: Page title (TEXT)
- `content`: Extracted text content (TEXT)
- `links_count`: Number of extracted links (INTEGER)
- `images_count`: Number of extracted images (INTEGER)
- `word_count`: Content word count (INTEGER)
- `scraped_at`: Timestamp (TIMESTAMP, INDEXED)

### 📈 system_metrics
Real-time and historical system performance data.
- `id`: Primary key (INTEGER)
- `cpu_percent`: CPU usage percentage (REAL)
- `memory_percent`: Memory usage percentage (REAL)
- `disk_usage`: Disk usage percentage (REAL)
- `network_io`: Network I/O statistics (TEXT)
- `process_count`: Active process count (INTEGER)
- `recorded_at`: Timestamp (TIMESTAMP, INDEXED)

### 🔄 api_cache
Intelligent API response caching with TTL management.
- `id`: Primary key (INTEGER)
- `endpoint`: API endpoint URL (TEXT, INDEXED)
- `method`: HTTP method (TEXT)
- `response_data`: Cached response (TEXT)
- `response_status`: HTTP status code (INTEGER)
- `response_size`: Response size in bytes (INTEGER)
- `cached_at`: Cache timestamp (TIMESTAMP, INDEXED)
- `expires_at`: Cache expiration (TIMESTAMP, INDEXED)

### 📁 file_operations
File operation history and metadata.
- `id`: Primary key (INTEGER)
- `operation_type`: Operation performed (TEXT)
- `file_path`: Target file/directory path (TEXT)
- `file_size`: File size in bytes (INTEGER)
- `operation_result`: Operation outcome (TEXT)
- `execution_time`: Time taken in seconds (REAL)
- `created_at`: Timestamp (TIMESTAMP, INDEXED)

## 🚨 Troubleshooting

### Common Installation Issues

#### Python Version Compatibility
```bash
# Check Python version
python --version

# If using Python 3.8 or older, upgrade:
# Windows: Download from python.org
# macOS: brew install python@3.11
# Ubuntu: sudo apt install python3.11
```

#### Missing Dependencies
```bash
# Install all dependencies
pip install -r requirements.txt

# For specific missing packages:
pip install mcp aiohttp pandas matplotlib seaborn beautifulsoup4 psutil requests

# If still having issues, try:
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

#### Permission Errors (Unix/Linux/macOS)
```bash
# Make script executable
chmod +x advanced_mcp_server.py

# Or run with python directly
python advanced_mcp_server.py
```

### MCP Configuration Issues

#### Server Not Starting
1. **Check MCP client logs** for error messages
2. **Verify file paths** in configuration are absolute
3. **Test server manually**:
   ```bash
   python advanced_mcp_server.py
   # Should show server startup messages
   ```

#### Import Errors in GitHub Mode
```json
// Add environment variables if needed
{
  "mcpServers": {
    "advanced-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/hezronkimutai/mcp_server.git", "python", "advanced_mcp_server.py"],
      "env": {
        "PYTHONPATH": ".",
        "PYTHONUNBUFFERED": "1"
      },
      "disabled": false
    }
  }
}
```

#### Tool Approval Issues
Make sure tools are in the `autoApprove` list:
```json
"autoApprove": [
  "scrape_website",
  "analyze_data", 
  "system_monitor",
  "file_operations",
  "api_integration",
  "database_query",
  "generate_report"
]
```

### Runtime Issues

#### Memory Usage
- **Large datasets**: Process in chunks using `limit` parameters
- **Long monitoring**: Use shorter intervals or duration
- **Database size**: Regular cleanup of old data

#### Network Timeouts
- **Increase timeout values** in API calls
- **Check firewall settings** for outbound connections
- **Use smaller batch sizes** for bulk operations

#### File Permission Errors
- **Windows**: Run as administrator if needed
- **Unix/Linux**: Check file/directory permissions
- **Use absolute paths** to avoid relative path issues

### Performance Optimization

#### Database Performance
```python
# Regular maintenance (add to cron job)
python -c "
import sqlite3
conn = sqlite3.connect('server.db')
conn.execute('VACUUM')
conn.execute('ANALYZE')
conn.close()
"
```

#### Memory Management
- Use streaming for large file operations
- Clear visualization plots after generation
- Implement result pagination for large queries

## 🔒 Security Considerations

### Data Protection
- **Database encryption**: Sensitive data is stored in local SQLite
- **API keys**: Store in environment variables, not in code
- **File access**: Server respects system file permissions
- **Input validation**: All inputs are sanitized and validated

### Network Security
- **HTTPS only**: API calls use secure connections
- **Rate limiting**: Built-in request throttling
- **Error handling**: Sensitive information not exposed in errors
- **Caching**: Sensitive API responses can be excluded from cache

### Best Practices
- **Regular updates**: Keep dependencies updated
- **Access control**: Limit MCP server access appropriately
- **Monitoring**: Use system monitoring for security events
- **Backups**: Regular database and configuration backups

## 🤝 Contributing

We welcome contributions! Here's how you can help improve the Advanced MCP Server:

### 🚀 Quick Start for Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp_server.git
   cd mcp_server
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Set up development environment**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

### 🛠️ Development Guidelines

#### Code Style
- **Follow PEP 8** Python style guidelines
- **Use type hints** for function parameters and returns
- **Add docstrings** for all functions and classes
- **Keep functions focused** and single-purpose

#### Testing
```bash
# Run tests (when available)
python -m pytest tests/

# Manual testing
python advanced_mcp_server.py --test-mode

# Integration testing with MCP client
```

#### Adding New Tools

1. **Define the tool** in `handle_list_tools()`:
```python
Tool(
    name="your_new_tool",
    description="Clear description of what it does",
    inputSchema={
        "type": "object",
        "properties": {
            "parameter_name": {
                "type": "string",
                "description": "Parameter description"
            }
        },
        "required": ["parameter_name"]
    }
)
```

2. **Implement the handler** in `handle_call_tool()`:
```python
elif request.params.name == "your_new_tool":
    return await self.your_new_tool_method(request.params.arguments)
```

3. **Create the method**:
```python
async def your_new_tool_method(self, args: Dict[str, Any]) -> List[types.TextContent]:
    """
    Implement your tool functionality here.
    
    Args:
        args: Dictionary of tool arguments
        
    Returns:
        List of TextContent with results
    """
    # Implementation here
    pass
```

4. **Update documentation** in README.md

#### Database Changes
- **Create migration scripts** for schema changes
- **Maintain backward compatibility** when possible
- **Document schema changes** in commit messages

### 📝 Commit Guidelines

Use conventional commits:
```bash
git commit -m "feat: add new data visualization tool"
git commit -m "fix: resolve database connection timeout"
git commit -m "docs: update API documentation"
git commit -m "refactor: optimize file search algorithm"
```

### 🐛 Bug Reports

When reporting bugs, please include:
- **Operating System** and Python version
- **MCP client** being used (Claude Desktop, etc.)
- **Error messages** and stack traces
- **Steps to reproduce** the issue
- **Expected vs actual behavior**

### 💡 Feature Requests

For new features, please:
- **Check existing issues** to avoid duplicates
- **Describe the use case** and problem you're solving
- **Provide examples** of how the feature would be used
- **Consider backward compatibility**

### 🔄 Pull Request Process

1. **Update documentation** as needed
2. **Add/update tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** if applicable
5. **Request review** from maintainers

### 📋 Development Roadmap

Planned features and improvements:
- [ ] **Multi-format data export** (Excel, Parquet, XML)
- [ ] **Advanced scheduling** for automated reports
- [ ] **Plugin system** for custom extensions
- [ ] **Web dashboard** for server management
- [ ] **Docker containerization** for easy deployment
- [ ] **Distributed caching** with Redis support
- [ ] **Machine learning** integration for data analysis
- [ ] **Real-time notifications** and alerting
- [ ] **Authentication and authorization** system
- [ ] **API rate limiting** per client
- [ ] **Comprehensive test suite** with CI/CD
- [ ] **Performance benchmarking** tools

## 🏗️ Repository Structure

```
mcp_server/
├── 📄 advanced_mcp_server.py      # Main MCP server implementation
├── 📄 requirements.txt            # Python dependencies
├── 📄 setup.py                   # Package configuration
├── 📄 README.md                  # This documentation
├── 📄 CHANGELOG.md               # Version history (planned)
├── 📄 LICENSE                    # MIT License (planned)
│
├── 🗂️ configs/                   # Configuration files
│   ├── 📄 github_mcp_config.json      # GitHub deployment config
│   ├── 📄 local_mcp_config.json       # Local development config
│   ├── 📄 mcp_config_direct.json      # Direct execution config
│   └── 📄 working_mcp_config.json     # Working configuration
│
├── 🗂️ docs/                      # Documentation (planned)
│   ├── 📄 mcp_github_configs.md       # GitHub configuration guide
│   ├── 📄 api_reference.md            # API documentation (planned)
│   ├── 📄 examples.md                 # Usage examples (planned)
│   └── 📄 troubleshooting.md          # Troubleshooting guide (planned)
│
├── 🗂️ scripts/                   # Utility scripts
│   ├── 📄 github_mcp_runner.py        # GitHub execution wrapper
│   └── 📄 run_github_mcp.py          # Alternative runner
│
├── 🗂️ tests/                     # Test suite (planned)
│   ├── 📄 test_server.py              # Server tests
│   ├── 📄 test_tools.py               # Tool functionality tests
│   └── 📄 test_integration.py         # Integration tests
│
└── 🗂️ examples/                  # Usage examples (planned)
    ├── 📄 basic_usage.py              # Basic server usage
    ├── 📄 advanced_analysis.py        # Complex data analysis
    └── 📄 custom_tools.py             # Custom tool development
```

### 📁 Key Files Description

- **`advanced_mcp_server.py`**: Core server implementation with all tools
- **`requirements.txt`**: All Python dependencies with version constraints
- **`setup.py`**: Package metadata and installation configuration
- **`github_mcp_runner.py`**: Wrapper for running server from GitHub
- **Config files**: Ready-to-use MCP configurations for different scenarios

## 🌟 Use Cases & Examples

### 📊 Business Intelligence Dashboard
```bash
# 1. Monitor system performance
{"duration_minutes": 60, "interval_seconds": 300, "save_metrics": true}

# 2. Analyze sales data
{"file_path": "/data/sales.csv", "analysis_type": "trends", "create_visualization": true}

# 3. Generate executive report
{"report_type": "data_summary", "format": "html", "include_charts": true}
```

### 🔍 Content Research & Analysis
```bash
# 1. Scrape competitor websites
{"url": "https://competitor.com", "extract_links": true, "save_to_db": true}

# 2. Analyze content patterns
{"query": "SELECT title, word_count FROM web_scrapes WHERE scraped_at > datetime('now', '-7 days')"}

# 3. Generate content report
{"report_type": "web_analysis", "format": "markdown", "time_range": "7_days"}
```

### 🔧 DevOps & System Administration
```bash
# 1. Monitor server health
{"duration_minutes": 1440, "interval_seconds": 600, "alert_thresholds": {"cpu": 80}}

# 2. Analyze log files
{"operation": "analyze", "path": "/var/log", "file_types": [".log"]}

# 3. Cleanup old files
{"operation": "cleanup", "path": "/tmp", "pattern": "*.tmp|*.cache"}
```

### 📈 Data Science Workflow
```bash
# 1. Import and analyze dataset
{"file_path": "/data/experiment.csv", "analysis_type": "summary"}

# 2. Generate correlation matrix
{"file_path": "/data/experiment.csv", "analysis_type": "correlation", "create_visualization": true}

# 3. Export results
{"query": "SELECT * FROM analysis_results", "format": "csv", "export_file": "/results/output.csv"}
```

## 📚 Related Projects & Resources

### 🔗 MCP Ecosystem
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Official MCP documentation
- **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** - Python SDK for MCP
- **[Claude Desktop](https://claude.ai/download)** - Popular MCP client

### 🛠️ Tools & Libraries Used
- **[aiohttp](https://docs.aiohttp.org/)** - Async HTTP client/server
- **[pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[matplotlib](https://matplotlib.org/)** - Data visualization
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing
- **[psutil](https://github.com/giampaolo/psutil)** - System monitoring

### 🎓 Learning Resources
- **[Python Async Programming](https://docs.python.org/3/library/asyncio.html)** - Asyncio documentation
- **[SQLite Tutorial](https://www.sqlitetutorial.net/)** - SQLite learning guide
- **[Data Analysis with Python](https://pandas.pydata.org/docs/user_guide/)** - Pandas user guide

## 🆕 Changelog

### Version 1.0.0 (Current)
- ✅ **Initial release** with core functionality
- ✅ **Web scraping** with content analysis
- ✅ **Data analysis** with visualizations
- ✅ **System monitoring** with metrics storage
- ✅ **File operations** with search capabilities
- ✅ **API integration** with caching
- ✅ **Database operations** with SQL support
- ✅ **Report generation** in multiple formats

### Planned for Version 1.1.0
- 🔄 **Enhanced error handling** and recovery
- 🔄 **Plugin architecture** for extensibility
- 🔄 **Web dashboard** for server management
- 🔄 **Docker support** for containerized deployment
- 🔄 **Advanced authentication** and authorization

### Planned for Version 1.2.0
- 🔄 **Machine learning** integration
- 🔄 **Real-time notifications** and alerts
- 🔄 **Distributed caching** with Redis
- 🔄 **Performance optimization** and benchmarking
- 🔄 **Comprehensive test suite** with CI/CD

## ⚖️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ **Commercial use** allowed
- ✅ **Modification** allowed
- ✅ **Distribution** allowed
- ✅ **Private use** allowed
- ❌ **No warranty** provided
- ❌ **No liability** assumed

## 🙏 Acknowledgments

### 💡 Inspiration & Thanks
- **[Anthropic](https://www.anthropic.com/)** for creating Claude and the MCP standard
- **[Model Context Protocol community](https://github.com/modelcontextprotocol)** for the excellent framework
- **Open source contributors** of all the amazing libraries used in this project
- **Early adopters and testers** who provided valuable feedback

### 🌟 Special Recognition
- **Python Software Foundation** for the incredible Python ecosystem
- **SQLite team** for the reliable embedded database
- **Matplotlib/Seaborn teams** for powerful visualization tools
- **pandas team** for making data analysis accessible

## 📞 Support & Community

### 🆘 Getting Help
- **📖 Documentation**: Start with this README and the `/docs` folder
- **🐛 Issues**: Report bugs and request features on [GitHub Issues](https://github.com/hezronkimutai/mcp_server/issues)
- **💬 Discussions**: Join the conversation on [GitHub Discussions](https://github.com/hezronkimutai/mcp_server/discussions)
- **📧 Email**: For private inquiries, contact the maintainers

### 🌍 Community Guidelines
- **Be respectful** and inclusive
- **Help others** learn and succeed
- **Share knowledge** and experiences
- **Contribute positively** to the ecosystem
- **Follow the code of conduct**

### 🔮 Future Vision
Our goal is to make the **Advanced MCP Server** the go-to solution for:
- **Data professionals** needing comprehensive analysis tools
- **Developers** requiring robust system integration
- **Businesses** seeking automated reporting and monitoring
- **Researchers** conducting data-driven investigations
- **DevOps teams** managing complex infrastructures

---

<div align="center">

**⭐ If this project helps you, please give it a star! ⭐**

**🚀 Ready to supercharge your MCP experience? Get started now! 🚀**

Made with ❤️ by the MCP Server community

</div>