
"""
Execution Script: Fetch Top Reddit Posts

Fetches recent posts from subreddits, filters by recency (7 days),
sorts by engagement, and saves the top 5 to a JSON file.
Uses standard library urllib to avoid dependencies.
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
from datetime import datetime
import traceback

# Constants
USER_AGENT = "script:top-posts-fetcher:v1.0 (by /u/conscious_agent)"
OUTPUT_FILE = os.path.join('.tmp', 'reddit_top_posts.json')
LOG_FILE = os.path.join('.tmp', 'fetch_log.txt')
DAYS_LOOKBACK = 7
TOP_N = 5
TIMEOUT = 10

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {msg}"
    print(entry, flush=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(entry + "\n")

def fetch_subreddit_posts(subreddit):
    """Fetches the 100 newest posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=100"
    log(f"Requesting URL: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                data = json.loads(content)
                posts = data.get('data', {}).get('children', [])
                log(f"Successfully fetched {len(posts)} posts from r/{subreddit}")
                return posts
            else:
                log(f"Error fetching r/{subreddit}: Status {response.status}")
                return []
    except urllib.error.HTTPError as e:
        log(f"HTTP Error fetching r/{subreddit}: {e.code} {e.reason}")
        return []
    except urllib.error.URLError as e:
        log(f"URL Error fetching r/{subreddit}: {e.reason}")
        return []
    except Exception as e:
        log(f"Exception fetching r/{subreddit}: {e}")
        log(traceback.format_exc())
        return []

def process_posts(posts):
    """Filters and sorts posts."""
    cutoff_date = datetime.now().timestamp() - (DAYS_LOOKBACK * 24 * 60 * 60)
    processed = []
    
    for post in posts:
        data = post.get('data', {})
        created_utc = data.get('created_utc', 0)
        
        # Filter by date (last 7 days)
        if created_utc < cutoff_date:
            continue
            
        engagement = data.get('score', 0) + data.get('num_comments', 0)
        
        processed.append({
            'title': data.get('title'),
            'url': data.get('url'),
            'permalink': f"https://www.reddit.com{data.get('permalink')}",
            'score': data.get('score'),
            'num_comments': data.get('num_comments'),
            'engagement': engagement,
            'created_utc': created_utc,
            'subreddit': data.get('subreddit')
        })
        
    # Sort by engagement (descending)
    processed.sort(key=lambda x: x['engagement'], reverse=True)
    
    return processed[:TOP_N]

def main():
    # Force unbuffered output
    sys.stdout.reconfigure(encoding='utf-8')
    
    # Ensure directories exist
    os.makedirs('.tmp', exist_ok=True)
    
    log("Starting fetch process...")
    
    if len(sys.argv) < 2:
        log("Usage: python fetch_reddit_posts.py <subreddit1> <subreddit2> ...")
        sys.exit(1)

    subreddits = sys.argv[1:]
    all_results = {}

    for sub in subreddits:
        log(f"Processing r/{sub}...")
        raw_posts = fetch_subreddit_posts(sub)
        top_posts = process_posts(raw_posts)
        all_results[sub] = top_posts
        log(f"Found {len(top_posts)} relevant posts in r/{sub}.")
        
        # Be nice to the API
        time.sleep(2)

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=4, ensure_ascii=False)
        log(f"Results saved to {OUTPUT_FILE}")
    except Exception as e:
        log(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
