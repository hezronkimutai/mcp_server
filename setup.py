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
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced Model Context Protocol (MCP) server with comprehensive capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hezronkimutai/mcp_server",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
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
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "advanced-mcp-server=advanced_mcp_server:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)