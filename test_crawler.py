#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify crawler imports work correctly
"""

import sys

try:
    import requests
    from bs4 import BeautifulSoup
    print("✓ Successfully imported requests and BeautifulSoup")
    
    # Test basic functionality
    print(f"requests version: {requests.__version__}")
    print(f"BeautifulSoup version: {BeautifulSoup.__version__ if hasattr(BeautifulSoup, '__version__') else 'unknown'}")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

print("\nCrawler dependencies are ready!")
