#!/usr/bin/env python3
"""
Advanced MCP Server with multiple capabilities:
- File system operations
- Web scraping and content analysis
- Data processing and visualization
- API integrations
- Database operations
- System monitoring
"""

import asyncio
import json
import sqlite3
import tempfile
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import logging

# Third-party imports
try:
    import aiohttp
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from bs4 import BeautifulSoup
    import psutil
    import requests
    from mcp.server.models import InitializationOptions
    from mcp.server import NotificationOptions, Server
    from mcp.server.stdio import stdio_server
    from mcp.types import (
        Resource,
        Tool,
        TextContent,
        ImageContent,
        EmbeddedResource,
        LoggingLevel
    )
    import mcp.types as types
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Install with: pip install mcp aiohttp pandas matplotlib seaborn beautifulsoup4 psutil requests")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("advanced-mcp-server")

class AdvancedMCPServer:
    def __init__(self):
        self.server = Server("advanced-mcp-server")
        self.db_path = tempfile.mktemp(suffix=".db")
        self.init_database()
        
    def init_database(self):
        """Initialize SQLite database for data storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables for different data types
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS web_scrapes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                title TEXT,
                content TEXT,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpu_percent REAL,
                memory_percent REAL,
                disk_usage REAL,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endpoint TEXT NOT NULL,
                response_data TEXT,
                cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()

    async def setup_handlers(self):
        """Setup all MCP handlers"""
        
        # List available tools
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            return [
                Tool(
                    name="scrape_website",
                    description="Scrape and analyze website content with advanced parsing",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "url": {"type": "string", "description": "URL to scrape"},
                            "extract_links": {"type": "boolean", "default": False},
                            "extract_images": {"type": "boolean", "default": False},
                            "save_to_db": {"type": "boolean", "default": True}
                        },
                        "required": ["url"]
                    }
                ),
                Tool(
                    name="analyze_data",
                    description="Perform statistical analysis on CSV data with visualizations",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string", "description": "Path to CSV file"},
                            "analysis_type": {
                                "type": "string", 
                                "enum": ["summary", "correlation", "distribution", "trends"],
                                "description": "Type of analysis to perform"
                            },
                            "create_visualization": {"type": "boolean", "default": True}
                        },
                        "required": ["file_path", "analysis_type"]
                    }
                ),
                Tool(
                    name="system_monitor",
                    description="Monitor system resources and performance metrics",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "duration_minutes": {"type": "integer", "default": 1},
                            "interval_seconds": {"type": "integer", "default": 10},
                            "save_metrics": {"type": "boolean", "default": True}
                        }
                    }
                ),
                Tool(
                    name="file_operations",
                    description="Advanced file system operations with search and analysis",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "operation": {
                                "type": "string",
                                "enum": ["search", "analyze", "backup", "cleanup", "compare"],
                                "description": "File operation to perform"
                            },
                            "path": {"type": "string", "description": "File or directory path"},
                            "pattern": {"type": "string", "description": "Search pattern (for search operation)"},
                            "options": {"type": "object", "description": "Additional options"}
                        },
                        "required": ["operation", "path"]
                    }
                ),
                Tool(
                    name="api_integration",
                    description="Make API calls with caching and error handling",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "endpoint": {"type": "string", "description": "API endpoint URL"},
                            "method": {"type": "string", "enum": ["GET", "POST", "PUT", "DELETE"], "default": "GET"},
                            "headers": {"type": "object", "description": "Request headers"},
                            "data": {"type": "object", "description": "Request body data"},
                            "use_cache": {"type": "boolean", "default": True},
                            "cache_duration_hours": {"type": "integer", "default": 1}
                        },
                        "required": ["endpoint"]
                    }
                ),
                Tool(
                    name="database_query",
                    description="Execute SQL queries on the internal database",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "SQL query to execute"},
                            "table": {"type": "string", "enum": ["web_scrapes", "system_metrics", "api_cache"]},
                            "limit": {"type": "integer", "default": 100}
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="generate_report",
                    description="Generate comprehensive reports from collected data",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "report_type": {
                                "type": "string",
                                "enum": ["system_health", "web_analysis", "data_summary"],
                                "description": "Type of report to generate"
                            },
                            "format": {"type": "string", "enum": ["html", "json", "markdown"], "default": "markdown"},
                            "include_charts": {"type": "boolean", "default": True}
                        },
                        "required": ["report_type"]
                    }
                )
            ]      
  # Tool call handlers
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
            try:
                if name == "scrape_website":
                    return await self.scrape_website(**arguments)
                elif name == "analyze_data":
                    return await self.analyze_data(**arguments)
                elif name == "system_monitor":
                    return await self.system_monitor(**arguments)
                elif name == "file_operations":
                    return await self.file_operations(**arguments)
                elif name == "api_integration":
                    return await self.api_integration(**arguments)
                elif name == "database_query":
                    return await self.database_query(**arguments)
                elif name == "generate_report":
                    return await self.generate_report(**arguments)
                else:
                    raise ValueError(f"Unknown tool: {name}")
            except Exception as e:
                logger.error(f"Error in tool {name}: {str(e)}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

    async def scrape_website(self, url: str, extract_links: bool = False, 
                           extract_images: bool = False, save_to_db: bool = True) -> List[TextContent]:
        """Advanced web scraping with content analysis"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return [TextContent(type="text", text=f"Failed to fetch {url}: HTTP {response.status}")]
                    
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Extract basic content
                    title = soup.find('title')
                    title_text = title.get_text().strip() if title else "No title found"
                    
                    # Remove script and style elements
                    for script in soup(["script", "style"]):
                        script.decompose()
                    
                    # Get text content
                    text_content = soup.get_text()
                    lines = (line.strip() for line in text_content.splitlines())
                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                    clean_text = ' '.join(chunk for chunk in chunks if chunk)
                    
                    result = {
                        "url": url,
                        "title": title_text,
                        "content_length": len(clean_text),
                        "word_count": len(clean_text.split()),
                        "content_preview": clean_text[:500] + "..." if len(clean_text) > 500 else clean_text
                    }
                    
                    # Extract links if requested
                    if extract_links:
                        links = []
                        for link in soup.find_all('a', href=True):
                            links.append({
                                "text": link.get_text().strip(),
                                "href": link['href']
                            })
                        result["links"] = links[:20]  # Limit to first 20 links
                    
                    # Extract images if requested
                    if extract_images:
                        images = []
                        for img in soup.find_all('img', src=True):
                            images.append({
                                "alt": img.get('alt', ''),
                                "src": img['src']
                            })
                        result["images"] = images[:10]  # Limit to first 10 images
                    
                    # Save to database if requested
                    if save_to_db:
                        conn = sqlite3.connect(self.db_path)
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO web_scrapes (url, title, content) VALUES (?, ?, ?)",
                            (url, title_text, clean_text)
                        )
                        conn.commit()
                        conn.close()
                        result["saved_to_db"] = True
                    
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                    
        except Exception as e:
            return [TextContent(type="text", text=f"Error scraping {url}: {str(e)}")]

    async def analyze_data(self, file_path: str, analysis_type: str, 
                          create_visualization: bool = True) -> List[TextContent | ImageContent]:
        """Perform statistical analysis on CSV data"""
        try:
            if not os.path.exists(file_path):
                return [TextContent(type="text", text=f"File not found: {file_path}")]
            
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            results = []
            analysis_result = {
                "file": file_path,
                "analysis_type": analysis_type,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns)
            }
            
            if analysis_type == "summary":
                analysis_result["summary"] = df.describe().to_dict()
                analysis_result["data_types"] = df.dtypes.to_dict()
                analysis_result["missing_values"] = df.isnull().sum().to_dict()
                
            elif analysis_type == "correlation":
                numeric_cols = df.select_dtypes(include=['number']).columns
                if len(numeric_cols) > 1:
                    correlation_matrix = df[numeric_cols].corr()
                    analysis_result["correlation_matrix"] = correlation_matrix.to_dict()
                    
                    if create_visualization:
                        plt.figure(figsize=(10, 8))
                        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
                        plt.title('Correlation Matrix')
                        
                        viz_path = tempfile.mktemp(suffix=".png")
                        plt.savefig(viz_path, dpi=150, bbox_inches='tight')
                        plt.close()
                        
                        with open(viz_path, 'rb') as f:
                            image_data = f.read()
                        
                        results.append(ImageContent(
                            type="image",
                            data=image_data,
                            mimeType="image/png"
                        ))
                        os.unlink(viz_path)
                else:
                    analysis_result["error"] = "Not enough numeric columns for correlation analysis"
                    
            elif analysis_type == "distribution":
                numeric_cols = df.select_dtypes(include=['number']).columns
                if len(numeric_cols) > 0:
                    for col in numeric_cols[:3]:  # Limit to first 3 columns
                        analysis_result[f"{col}_distribution"] = {
                            "mean": float(df[col].mean()),
                            "median": float(df[col].median()),
                            "std": float(df[col].std()),
                            "min": float(df[col].min()),
                            "max": float(df[col].max())
                        }
                    
                    if create_visualization:
                        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
                        axes = axes.ravel()
                        
                        for i, col in enumerate(numeric_cols[:4]):
                            df[col].hist(bins=30, ax=axes[i])
                            axes[i].set_title(f'Distribution of {col}')
                            axes[i].set_xlabel(col)
                            axes[i].set_ylabel('Frequency')
                        
                        plt.tight_layout()
                        
                        viz_path = tempfile.mktemp(suffix=".png")
                        plt.savefig(viz_path, dpi=150, bbox_inches='tight')
                        plt.close()
                        
                        with open(viz_path, 'rb') as f:
                            image_data = f.read()
                        
                        results.append(ImageContent(
                            type="image",
                            data=image_data,
                            mimeType="image/png"
                        ))
                        os.unlink(viz_path)
                        
            elif analysis_type == "trends":
                # Look for date columns and numeric columns for trend analysis
                date_cols = df.select_dtypes(include=['datetime64']).columns
                if len(date_cols) == 0:
                    # Try to parse date columns
                    for col in df.columns:
                        if 'date' in col.lower() or 'time' in col.lower():
                            try:
                                df[col] = pd.to_datetime(df[col])
                                date_cols = [col]
                                break
                            except:
                                continue
                
                numeric_cols = df.select_dtypes(include=['number']).columns
                
                if len(date_cols) > 0 and len(numeric_cols) > 0:
                    date_col = date_cols[0]
                    df_sorted = df.sort_values(date_col)
                    
                    analysis_result["trend_analysis"] = {
                        "date_column": date_col,
                        "date_range": {
                            "start": str(df_sorted[date_col].min()),
                            "end": str(df_sorted[date_col].max())
                        }
                    }
                    
                    if create_visualization:
                        plt.figure(figsize=(12, 8))
                        for col in numeric_cols[:3]:  # Limit to first 3 numeric columns
                            plt.plot(df_sorted[date_col], df_sorted[col], label=col, marker='o', markersize=3)
                        
                        plt.title('Trends Over Time')
                        plt.xlabel(date_col)
                        plt.ylabel('Values')
                        plt.legend()
                        plt.xticks(rotation=45)
                        
                        viz_path = tempfile.mktemp(suffix=".png")
                        plt.savefig(viz_path, dpi=150, bbox_inches='tight')
                        plt.close()
                        
                        with open(viz_path, 'rb') as f:
                            image_data = f.read()
                        
                        results.append(ImageContent(
                            type="image",
                            data=image_data,
                            mimeType="image/png"
                        ))
                        os.unlink(viz_path)
                else:
                    analysis_result["error"] = "No suitable date and numeric columns found for trend analysis"
            
            results.insert(0, TextContent(type="text", text=json.dumps(analysis_result, indent=2)))
            return results
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error analyzing data: {str(e)}")]

    async def system_monitor(self, duration_minutes: int = 1, interval_seconds: int = 10, 
                           save_metrics: bool = True) -> List[TextContent]:
        """Monitor system resources and performance"""
        try:
            metrics = []
            end_time = datetime.now() + timedelta(minutes=duration_minutes)
            
            while datetime.now() < end_time:
                # Collect system metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                
                metric = {
                    "timestamp": datetime.now().isoformat(),
                    "cpu_percent": cpu_percent,
                    "memory_percent": memory.percent,
                    "memory_available_gb": round(memory.available / (1024**3), 2),
                    "disk_usage_percent": disk.percent,
                    "disk_free_gb": round(disk.free / (1024**3), 2)
                }
                
                metrics.append(metric)
                
                # Save to database if requested
                if save_metrics:
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO system_metrics (cpu_percent, memory_percent, disk_usage) VALUES (?, ?, ?)",
                        (cpu_percent, memory.percent, disk.percent)
                    )
                    conn.commit()
                    conn.close()
                
                if datetime.now() < end_time:
                    await asyncio.sleep(interval_seconds)
            
            # Calculate summary statistics
            if metrics:
                cpu_values = [m["cpu_percent"] for m in metrics]
                memory_values = [m["memory_percent"] for m in metrics]
                
                summary = {
                    "monitoring_duration_minutes": duration_minutes,
                    "samples_collected": len(metrics),
                    "cpu_stats": {
                        "average": round(sum(cpu_values) / len(cpu_values), 2),
                        "max": max(cpu_values),
                        "min": min(cpu_values)
                    },
                    "memory_stats": {
                        "average": round(sum(memory_values) / len(memory_values), 2),
                        "max": max(memory_values),
                        "min": min(memory_values)
                    },
                    "detailed_metrics": metrics
                }
                
                return [TextContent(type="text", text=json.dumps(summary, indent=2))]
            else:
                return [TextContent(type="text", text="No metrics collected")]
                
        except Exception as e:
            return [TextContent(type="text", text=f"Error monitoring system: {str(e)}")]

    async def file_operations(self, operation: str, path: str, pattern: str = None, 
                            options: Dict = None) -> List[TextContent]:
        """Advanced file system operations"""
        try:
            if options is None:
                options = {}
                
            result = {"operation": operation, "path": path}
            
            if operation == "search":
                if not pattern:
                    return [TextContent(type="text", text="Pattern required for search operation")]
                
                matches = []
                search_path = Path(path)
                
                if search_path.is_file():
                    # Search within a single file
                    with open(search_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern.lower() in line.lower():
                                matches.append({
                                    "file": str(search_path),
                                    "line": line_num,
                                    "content": line.strip()
                                })
                elif search_path.is_dir():
                    # Search within directory
                    for file_path in search_path.rglob("*"):
                        if file_path.is_file() and file_path.suffix in ['.txt', '.py', '.js', '.html', '.css', '.md']:
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    for line_num, line in enumerate(f, 1):
                                        if pattern.lower() in line.lower():
                                            matches.append({
                                                "file": str(file_path),
                                                "line": line_num,
                                                "content": line.strip()
                                            })
                                            if len(matches) >= 100:  # Limit results
                                                break
                            except:
                                continue
                
                result["matches"] = matches[:50]  # Limit to 50 matches
                result["total_matches"] = len(matches)
                
            elif operation == "analyze":
                path_obj = Path(path)
                if path_obj.is_file():
                    stat = path_obj.stat()
                    result.update({
                        "type": "file",
                        "size_bytes": stat.st_size,
                        "size_mb": round(stat.st_size / (1024*1024), 2),
                        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                        "extension": path_obj.suffix
                    })
                    
                    # Analyze content if it's a text file
                    if path_obj.suffix in ['.txt', '.py', '.js', '.html', '.css', '.md']:
                        try:
                            with open(path_obj, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                result.update({
                                    "lines": len(content.splitlines()),
                                    "characters": len(content),
                                    "words": len(content.split())
                                })
                        except:
                            result["content_analysis"] = "Unable to read file content"
                            
                elif path_obj.is_dir():
                    files = list(path_obj.rglob("*"))
                    file_types = {}
                    total_size = 0
                    
                    for file_path in files:
                        if file_path.is_file():
                            ext = file_path.suffix or "no_extension"
                            file_types[ext] = file_types.get(ext, 0) + 1
                            total_size += file_path.stat().st_size
                    
                    result.update({
                        "type": "directory",
                        "total_files": len([f for f in files if f.is_file()]),
                        "total_directories": len([f for f in files if f.is_dir()]),
                        "total_size_mb": round(total_size / (1024*1024), 2),
                        "file_types": file_types
                    })
                    
            elif operation == "backup":
                # Simple backup operation
                import shutil
                backup_path = f"{path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                
                if Path(path).is_file():
                    shutil.copy2(path, backup_path)
                elif Path(path).is_dir():
                    shutil.copytree(path, backup_path)
                
                result["backup_created"] = backup_path
                
            elif operation == "cleanup":
                # Clean up temporary files
                cleaned_files = []
                path_obj = Path(path)
                
                if path_obj.is_dir():
                    for file_path in path_obj.rglob("*"):
                        if file_path.is_file() and (
                            file_path.suffix in ['.tmp', '.temp', '.log'] or
                            file_path.name.startswith('~') or
                            file_path.name.endswith('.bak')
                        ):
                            try:
                                file_path.unlink()
                                cleaned_files.append(str(file_path))
                            except:
                                continue
                
                result["cleaned_files"] = cleaned_files
                result["files_removed"] = len(cleaned_files)
            
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error in file operation: {str(e)}")]

    async def api_integration(self, endpoint: str, method: str = "GET", headers: Dict = None,
                            data: Dict = None, use_cache: bool = True, 
                            cache_duration_hours: int = 1) -> List[TextContent]:
        """Make API calls with caching and error handling"""
        try:
            # Check cache first
            if use_cache and method == "GET":
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT response_data, cached_at FROM api_cache WHERE endpoint = ? AND cached_at > ?",
                    (endpoint, datetime.now() - timedelta(hours=cache_duration_hours))
                )
                cached_result = cursor.fetchone()
                conn.close()
                
                if cached_result:
                    return [TextContent(type="text", text=f"Cached response:\n{cached_result[0]}")]
            
            # Make the API call
            async with aiohttp.ClientSession() as session:
                kwargs = {
                    'url': endpoint,
                    'headers': headers or {}
                }
                
                if method in ['POST', 'PUT'] and data:
                    kwargs['json'] = data
                
                async with session.request(method, **kwargs) as response:
                    response_text = await response.text()
                    
                    result = {
                        "endpoint": endpoint,
                        "method": method,
                        "status_code": response.status,
                        "headers": dict(response.headers),
                        "response": response_text
                    }
                    
                    # Try to parse JSON response
                    try:
                        result["parsed_response"] = json.loads(response_text)
                    except:
                        result["parsed_response"] = "Not valid JSON"
                    
                    # Cache successful GET requests
                    if use_cache and method == "GET" and response.status == 200:
                        conn = sqlite3.connect(self.db_path)
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO api_cache (endpoint, response_data) VALUES (?, ?)",
                            (endpoint, json.dumps(result))
                        )
                        conn.commit()
                        conn.close()
                    
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                    
        except Exception as e:
            return [TextContent(type="text", text=f"Error making API call: {str(e)}")]

    async def database_query(self, query: str, table: str = None, limit: int = 100) -> List[TextContent]:
        """Execute SQL queries on the internal database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Add LIMIT clause if not present
            if "LIMIT" not in query.upper() and "SELECT" in query.upper():
                query += f" LIMIT {limit}"
            
            cursor.execute(query)
            
            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                
                result = {
                    "query": query,
                    "columns": columns,
                    "row_count": len(results),
                    "data": [dict(zip(columns, row)) for row in results]
                }
            else:
                conn.commit()
                result = {
                    "query": query,
                    "rows_affected": cursor.rowcount,
                    "message": "Query executed successfully"
                }
            
            conn.close()
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Database error: {str(e)}")]

    async def generate_report(self, report_type: str, format: str = "markdown", 
                            include_charts: bool = True) -> List[TextContent | ImageContent]:
        """Generate comprehensive reports from collected data"""
        try:
            conn = sqlite3.connect(self.db_path)
            results = []
            
            if report_type == "system_health":
                # Get recent system metrics
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM system_metrics 
                    ORDER BY recorded_at DESC 
                    LIMIT 100
                """)
                metrics = cursor.fetchall()
                
                if metrics:
                    # Calculate health statistics
                    cpu_values = [m[1] for m in metrics]
                    memory_values = [m[2] for m in metrics]
                    disk_values = [m[3] for m in metrics]
                    
                    health_report = {
                        "report_type": "System Health Report",
                        "generated_at": datetime.now().isoformat(),
                        "metrics_analyzed": len(metrics),
                        "cpu_analysis": {
                            "average": round(sum(cpu_values) / len(cpu_values), 2),
                            "max": max(cpu_values),
                            "min": min(cpu_values),
                            "status": "Good" if sum(cpu_values) / len(cpu_values) < 80 else "Warning"
                        },
                        "memory_analysis": {
                            "average": round(sum(memory_values) / len(memory_values), 2),
                            "max": max(memory_values),
                            "min": min(memory_values),
                            "status": "Good" if sum(memory_values) / len(memory_values) < 85 else "Warning"
                        },
                        "disk_analysis": {
                            "average": round(sum(disk_values) / len(disk_values), 2),
                            "max": max(disk_values),
                            "min": min(disk_values),
                            "status": "Good" if sum(disk_values) / len(disk_values) < 90 else "Warning"
                        }
                    }
                    
                    if format == "markdown":
                        report_text = f"""# System Health Report
Generated: {health_report['generated_at']}

## CPU Usage
- Average: {health_report['cpu_analysis']['average']}%
- Max: {health_report['cpu_analysis']['max']}%
- Min: {health_report['cpu_analysis']['min']}%
- Status: {health_report['cpu_analysis']['status']}

## Memory Usage
- Average: {health_report['memory_analysis']['average']}%
- Max: {health_report['memory_analysis']['max']}%
- Min: {health_report['memory_analysis']['min']}%
- Status: {health_report['memory_analysis']['status']}

## Disk Usage
- Average: {health_report['disk_analysis']['average']}%
- Max: {health_report['disk_analysis']['max']}%
- Min: {health_report['disk_analysis']['min']}%
- Status: {health_report['disk_analysis']['status']}

## Recommendations
"""
                        if health_report['cpu_analysis']['average'] > 80:
                            report_text += "- Consider investigating high CPU usage processes\n"
                        if health_report['memory_analysis']['average'] > 85:
                            report_text += "- Memory usage is high, consider closing unnecessary applications\n"
                        if health_report['disk_analysis']['average'] > 90:
                            report_text += "- Disk space is running low, consider cleanup\n"
                        
                        results.append(TextContent(type="text", text=report_text))
                    else:
                        results.append(TextContent(type="text", text=json.dumps(health_report, indent=2)))
                    
                    # Create visualization if requested
                    if include_charts:
                        plt.figure(figsize=(12, 8))
                        
                        plt.subplot(2, 2, 1)
                        plt.plot(cpu_values[-50:])  # Last 50 measurements
                        plt.title('CPU Usage Over Time')
                        plt.ylabel('CPU %')
                        
                        plt.subplot(2, 2, 2)
                        plt.plot(memory_values[-50:])
                        plt.title('Memory Usage Over Time')
                        plt.ylabel('Memory %')
                        
                        plt.subplot(2, 2, 3)
                        plt.plot(disk_values[-50:])
                        plt.title('Disk Usage Over Time')
                        plt.ylabel('Disk %')
                        
                        plt.subplot(2, 2, 4)
                        # Summary pie chart
                        avg_values = [
                            health_report['cpu_analysis']['average'],
                            health_report['memory_analysis']['average'],
                            health_report['disk_analysis']['average']
                        ]
                        plt.pie(avg_values, labels=['CPU', 'Memory', 'Disk'], autopct='%1.1f%%')
                        plt.title('Average Resource Usage')
                        
                        plt.tight_layout()
                        
                        viz_path = tempfile.mktemp(suffix=".png")
                        plt.savefig(viz_path, dpi=150, bbox_inches='tight')
                        plt.close()
                        
                        with open(viz_path, 'rb') as f:
                            image_data = f.read()
                        
                        results.append(ImageContent(
                            type="image",
                            data=image_data,
                            mimeType="image/png"
                        ))
                        os.unlink(viz_path)
                else:
                    results.append(TextContent(type="text", text="No system metrics available for report"))
                    
            elif report_type == "web_analysis":
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT url, title, LENGTH(content) as content_length, scraped_at 
                    FROM web_scrapes 
                    ORDER BY scraped_at DESC 
                    LIMIT 50
                """)
                scrapes = cursor.fetchall()
                
                if scrapes:
                    web_report = {
                        "report_type": "Web Scraping Analysis",
                        "generated_at": datetime.now().isoformat(),
                        "total_scrapes": len(scrapes),
                        "scrapes": [
                            {
                                "url": s[0],
                                "title": s[1],
                                "content_length": s[2],
                                "scraped_at": s[3]
                            } for s in scrapes
                        ]
                    }
                    
                    if format == "markdown":
                        report_text = f"""# Web Scraping Analysis Report
Generated: {web_report['generated_at']}
Total Scrapes: {web_report['total_scrapes']}

## Recent Scrapes
"""
                        for scrape in scrapes[:10]:  # Show top 10
                            report_text += f"- **{scrape[1]}** ({scrape[0]})\n"
                            report_text += f"  - Content Length: {scrape[2]} characters\n"
                            report_text += f"  - Scraped: {scrape[3]}\n\n"
                        
                        results.append(TextContent(type="text", text=report_text))
                    else:
                        results.append(TextContent(type="text", text=json.dumps(web_report, indent=2)))
                else:
                    results.append(TextContent(type="text", text="No web scraping data available for report"))
                    
            elif report_type == "data_summary":
                # Get summary of all data in the database
                cursor = conn.cursor()
                
                # Count records in each table
                tables = ["web_scrapes", "system_metrics", "api_cache"]
                summary = {
                    "report_type": "Data Summary Report",
                    "generated_at": datetime.now().isoformat(),
                    "database_path": self.db_path
                }
                
                for table in tables:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    count = cursor.fetchone()[0]
                    summary[f"{table}_count"] = count
                
                if format == "markdown":
                    report_text = f"""# Data Summary Report
Generated: {summary['generated_at']}

## Database Statistics
- Web Scrapes: {summary['web_scrapes_count']} records
- System Metrics: {summary['system_metrics_count']} records  
- API Cache: {summary['api_cache_count']} records

## Database Location
{summary['database_path']}
"""
                    results.append(TextContent(type="text", text=report_text))
                else:
                    results.append(TextContent(type="text", text=json.dumps(summary, indent=2)))
            
            conn.close()
            return results
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error generating report: {str(e)}")]

async def main():
    """Main function to run the MCP server"""
    server_instance = AdvancedMCPServer()
    await server_instance.setup_handlers()
    
    # Run the server using stdio transport
    async with stdio_server() as (read_stream, write_stream):
        await server_instance.server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="advanced-mcp-server",
                server_version="1.0.0",
                capabilities=server_instance.server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())