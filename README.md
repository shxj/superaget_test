# 163.com News Crawler

A Python web crawler for extracting news articles from www.163.com.

## Features

- Fetches news articles from 163.com main news pages
- Extracts article titles, URLs, and summaries
- Saves results in JSON format
- Respects robots.txt and includes proper headers

## Requirements

- Python 3.7+
- requests library
- beautifulsoup4 library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python crawler_163_news.py
```

Or specify number of articles to crawl:

```bash
python crawler_163_news.py 10
```

## Notes

- This crawler is designed to be respectful of 163.com's terms of service
- It includes delays between requests to avoid overloading the server
- The parsing logic adapts to common 163.com HTML structures
- Results are saved to `163_news.json` in the current directory

## Disclaimer

This tool is for educational and research purposes only. Please ensure compliance with 163.com's terms of service and robots.txt before use.
