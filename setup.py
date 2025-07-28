#!/usr/bin/env python3
"""
Setup script for Advanced MCP Server
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="advanced-mcp-server",
    version="1.0.0",
    author="Hezron Kimutai",
    author_email="hezron.kimutai@example.com",
    description="Advanced Model Context Protocol (MCP) server with comprehensive capabilities for web scraping, data analysis, system monitoring, and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hezronkimutai/mcp_server",
    project_urls={
        "Bug Reports": "https://github.com/hezronkimutai/mcp_server/issues",
        "Source": "https://github.com/hezronkimutai/mcp_server",
        "Documentation": "https://github.com/hezronkimutai/mcp_server#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: System :: Monitoring",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Scientific/Engineering :: Visualization",
        "Environment :: Console",
        "Framework :: AsyncIO",
    ],
    keywords="mcp model-context-protocol web-scraping data-analysis system-monitoring api-integration database sqlite",
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.991",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "advanced-mcp-server=advanced_mcp_server:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)