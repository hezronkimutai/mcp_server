# Contributing to Advanced MCP Server

Thank you for your interest in contributing to the Advanced MCP Server! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Make** your changes
5. **Test** your changes
6. **Submit** a pull request

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of asyncio and MCP

### Local Development
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mcp_server.git
cd mcp_server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (when available)
pip install pytest black flake8 mypy

# Make the script executable (Unix/Linux/macOS)
chmod +x advanced_mcp_server.py
```

### Testing Your Changes
```bash
# Manual testing
python advanced_mcp_server.py

# With MCP client (Claude Desktop, etc.)
# Add your local server to MCP configuration and test

# Run automated tests (when available)
python -m pytest tests/
```

## 📝 Code Guidelines

### Code Style
- Follow **PEP 8** Python style guidelines
- Use **type hints** for all function parameters and return values
- Write **clear docstrings** for all public functions and classes
- Keep **functions focused** and under 50 lines when possible
- Use **meaningful variable names**

### Example Function
```python
async def example_tool(self, args: Dict[str, Any]) -> List[types.TextContent]:
    """
    Example tool implementation.
    
    Args:
        args: Dictionary containing tool arguments
            - required_param (str): Description of required parameter
            - optional_param (int, optional): Description of optional parameter
    
    Returns:
        List of TextContent objects with results
        
    Raises:
        ValueError: If required parameters are missing
        RuntimeError: If tool execution fails
    """
    # Validate inputs
    if "required_param" not in args:
        raise ValueError("required_param is required")
    
    # Implementation here
    result = await some_async_operation(args["required_param"])
    
    return [types.TextContent(
        type="text",
        text=f"Operation completed: {result}"
    )]
```

### Database Guidelines
- Use **parameterized queries** to prevent SQL injection
- **Close connections** properly in try/finally blocks
- **Index frequently queried columns**
- **Document schema changes** in migration scripts

### Error Handling
- Use **specific exception types** when possible
- **Log errors** with appropriate severity levels
- **Provide helpful error messages** to users
- **Clean up resources** in finally blocks

## 🔧 Adding New Tools

### Step 1: Define the Tool
Add your tool definition to the `handle_list_tools()` method:

```python
Tool(
    name="your_new_tool",
    description="Clear, concise description of what the tool does",
    inputSchema={
        "type": "object",
        "properties": {
            "parameter_name": {
                "type": "string",
                "description": "Description of this parameter"
            },
            "optional_param": {
                "type": "boolean",
                "description": "Optional parameter description",
                "default": False
            }
        },
        "required": ["parameter_name"]
    }
)
```

### Step 2: Add Tool Handler
Add the handler in `handle_call_tool()`:

```python
elif request.params.name == "your_new_tool":
    return await self.your_new_tool_method(request.params.arguments)
```

### Step 3: Implement the Method
Create the implementation method:

```python
async def your_new_tool_method(self, args: Dict[str, Any]) -> List[types.TextContent]:
    """Implementation of your new tool."""
    # Your implementation here
    pass
```

### Step 4: Update Documentation
- Add tool description to README.md
- Include usage examples
- Document any new dependencies

## 🐛 Bug Reports

When reporting bugs, please include:

### System Information
- Operating system and version
- Python version
- MCP client being used
- Server version or commit hash

### Bug Description
- **Clear title** summarizing the issue
- **Steps to reproduce** the bug
- **Expected behavior**
- **Actual behavior**
- **Error messages** and stack traces
- **Relevant configuration** (sanitized)

### Example Bug Report
```
**Title:** Web scraping fails with timeout on large pages

**Environment:**
- OS: Windows 11
- Python: 3.11.5
- MCP Client: Claude Desktop 1.2.3
- Server: commit abc123

**Steps to Reproduce:**
1. Call scrape_website tool
2. Use URL: https://example.com/large-page
3. Error occurs after 30 seconds

**Expected:** Page content should be scraped successfully
**Actual:** Timeout error occurs

**Error Message:**
```
TimeoutError: Request timed out after 30 seconds
```

**Additional Context:**
Page is approximately 5MB in size
```

## 💡 Feature Requests

### Before Submitting
- **Search existing issues** to avoid duplicates
- **Consider the scope** - is this a general-purpose feature?
- **Think about implementation** - how would this work?

### Feature Request Template
```
**Title:** Clear, descriptive feature title

**Problem:**
Describe the problem this feature would solve

**Proposed Solution:**
Detailed description of the proposed feature

**Use Cases:**
Specific examples of how this would be used

**Alternative Solutions:**
Other ways this problem could be solved

**Additional Context:**
Any other relevant information
```

## 🔄 Pull Request Process

### Before Submitting
1. **Update documentation** as needed
2. **Add or update tests** for new functionality
3. **Ensure all tests pass**
4. **Run linting** and fix any issues
5. **Update CHANGELOG.md** if applicable

### Pull Request Template
```
**Description:**
Brief description of changes

**Type of Change:**
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

**Testing:**
- [ ] Manual testing completed
- [ ] Automated tests pass
- [ ] Integration testing with MCP client

**Checklist:**
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

### Review Process
1. **Automated checks** must pass
2. **Maintainer review** required
3. **Address feedback** promptly
4. **Squash commits** if requested
5. **Merge** after approval

## 📚 Development Resources

### MCP Documentation
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification)
- [Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Client Integration](https://modelcontextprotocol.io/clients)

### Python Resources
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Type Hints Guide](https://docs.python.org/3/library/typing.html)
- [SQLite Python Tutorial](https://docs.python.org/3/library/sqlite3.html)

### Development Tools
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linting](https://flake8.pycqa.org/)
- [MyPy Type Checking](https://mypy.readthedocs.io/)
- [Pytest Testing](https://pytest.org/)

## 🎯 Development Priorities

### High Priority
- **Performance optimization** for large datasets
- **Error handling improvements**
- **Test suite development**
- **Documentation completion**

### Medium Priority
- **Plugin architecture** for extensibility
- **Advanced caching strategies**
- **Web dashboard interface**
- **Docker containerization**

### Future Considerations
- **Machine learning integration**
- **Distributed deployment**
- **Real-time notifications**
- **Advanced authentication**

## 🌟 Recognition

### Contributors
All contributors will be recognized in:
- **README.md acknowledgments**
- **GitHub contributors page**
- **Release notes** for significant contributions

### Types of Contributions
- **Code contributions** (features, bug fixes)
- **Documentation improvements**
- **Bug reports and testing**
- **Feature suggestions and design**
- **Community support and help**

Thank you for contributing to the Advanced MCP Server! 🚀
