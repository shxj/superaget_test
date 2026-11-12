#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web crawler for www.163.com news

This script crawls the main news page of 163.com and extracts article information.
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import sys
from urllib.parse import urljoin, urlparse

# Set headers to mimic a real browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


def fetch_news_page(url):
    """
    Fetch the HTML content of the news page
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        # Ensure proper encoding for Chinese characters
        response.encoding = response.apparent_encoding
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_news_articles(html_content):
    """
    Parse HTML content to extract news articles
    """
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []
    
    # Look for common news article containers on 163.com
    # 163.com typically uses divs with class names like 'news-item', 'ndi_main', 'post_item'
    # Also look for links in news lists
    
    # Try multiple selectors that might be used on 163.com
    selectors = [
        'div[data-role="news-item"]',
        'div.news-item',
        'div.ndi_main',
        'div.post_item',
        'div.list_item',
        'div.news-list > div',
        'ul.news-list li',
        'div.article',
        'div[data-sudaclick="newslist"]',
        'div[data-sudaclick^="newslist"]'
    ]
    
    for selector in selectors:
        elements = soup.select(selector)
        if elements:
            break
    else:
        # If no elements found with specific selectors, try general approach
        # Look for links with news-related text
        elements = soup.find_all(['a', 'div', 'h2', 'h3'], href=True)
    
    # Extract article information
    for element in elements[:20]:  # Limit to first 20 articles
        try:
            # Try to get title and link
            title_elem = element.find(['h2', 'h3', 'h4', 'a', 'div']) or element
            
            # Get title text
            title = title_elem.get_text(strip=True) if title_elem else ""
            
            # Get link
            link_elem = element.find('a') or element
            href = link_elem.get('href') if link_elem else None
            
            if href and not href.startswith('http'):
                href = urljoin('https://www.163.com/', href)
            
            # Skip if no title or link
            if not title or not href or len(title) < 5:
                continue
            
            # Get summary if available
            summary_elem = element.find(['p', 'div'], class_=['summary', 'desc', 'intro'])
            summary = summary_elem.get_text(strip=True) if summary_elem else ""
            
            # Clean up title and summary
            title = title.strip()
            summary = summary.strip()
            
            if title and href:
                articles.append({
                    'title': title,
                    'url': href,
                    'summary': summary,
                    'source': '163.com'
                })
                
        except Exception as e:
            continue
    
    return articles


def crawl_163_news(max_articles=20):
    """
    Main function to crawl 163.com news
    """
    print("Starting 163.com news crawler...")
    
    # Main 163.com news URL
    base_url = 'https://www.163.com/'
    
    # Try different URLs that might contain news
    urls_to_try = [
        'https://www.163.com/',
        'https://news.163.com/',
        'https://www.163.com/news/',
        'https://news.163.com/world/',
        'https://news.163.com/domestic/',
    ]
    
    all_articles = []
    
    for url in urls_to_try:
        print(f"Fetching {url}...")
        html_content = fetch_news_page(url)
        
        if html_content:
            articles = parse_news_articles(html_content)
            print(f"Found {len(articles)} articles on {url}")
            all_articles.extend(articles)
            
            # Stop if we have enough articles
            if len(all_articles) >= max_articles:
                break
        
        # Be respectful with rate limiting
        time.sleep(1)
    
    # Remove duplicates based on URL
    seen_urls = set()
    unique_articles = []
    for article in all_articles:
        if article['url'] not in seen_urls:
            seen_urls.add(article['url'])
            unique_articles.append(article)
    
    # Limit to max_articles
    unique_articles = unique_articles[:max_articles]
    
    return unique_articles


def save_articles_to_json(articles, filename='163_news.json'):
    """
    Save articles to JSON file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(articles)} articles to {filename}")
        return True
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
        return False


def main():
    """
    Main execution function
    """
    if len(sys.argv) > 1:
        try:
            max_articles = int(sys.argv[1])
        except ValueError:
            max_articles = 20
    else:
        max_articles = 20
    
    articles = crawl_163_news(max_articles)
    
    if articles:
        print(f"\nSuccessfully crawled {len(articles)} news articles from 163.com")
        print("\nSample articles:")
        for i, article in enumerate(articles[:3]):
            print(f"{i+1}. {article['title']}")
            print(f"   URL: {article['url']}")
            if article['summary']:
                print(f"   Summary: {article['summary'][:100]}...")
            print()
        
        # Save to JSON
        save_articles_to_json(articles)
        
        # Also print basic stats
        print(f"\nCrawling completed. Total articles: {len(articles)}")
    else:
        print("No articles found. This may be due to website structure changes or blocking.")

if __name__ == "__main__":
    main()
