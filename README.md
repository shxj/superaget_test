# 163.com News Crawler

A Python web crawler for extracting news articles from www.163.com.

## Features

- Fetches news articles from 163.com main news pages
- Extracts article titles, URLs, and summaries
- Saves results in JSON format
- Respects robots.txt and includes proper headers
- Quicksort functionality for sorting news articles by various criteria (title, date, relevance)

## Quicksort Functionality

The quicksort algorithm implementation provides efficient sorting capabilities for news articles:

- **Time Complexity**: O(n log n) average case, O(n²) worst case
- **Space Complexity**: O(log n) for the recursive implementation
- **In-place sorting**: Memory-efficient sorting option available
- **Flexible usage**: Can sort any list of comparable elements

### Usage Examples

```python
# Sort a list of numbers
numbers = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_numbers = quicksort(numbers)

# Sort news articles by title
articles = [
    {'title': 'News about AI', 'url': 'https://example.com/ai'},
    {'title': 'Technology updates', 'url': 'https://example.com/tech'}
]
# Sort by title (requires custom key function)
```

### Implementation Details

The quicksort module (`quicksort.py`) includes:

- `quicksort(arr)`: Returns a new sorted list
- `quicksort_inplace(arr, low=0, high=None)`: Sorts the list in-place
- `partition(arr, low, high)`: Helper function for partitioning

The algorithm uses the "divide and conquer" approach with a pivot element to efficiently sort data.

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
