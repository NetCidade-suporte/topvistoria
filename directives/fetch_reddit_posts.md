
# Directive: Fetch Top Reddit Posts

## Goal
Fetch recent posts from specified subreddits, identify the most engaging ones from the past week, and save them.

## Inputs
- `subreddits`: A list of subreddit names (e.g., `["n8n", "automation"]`).

## Tools
- `execution/fetch_reddit_posts.py`

## Instructions
1.  Run `execution/fetch_reddit_posts.py` passing the subreddit names as arguments.
    - Example: `python execution/fetch_reddit_posts.py n8n automation`
2.  The script will:
    - Fetch the 100 newest posts for each subreddit.
    - Filter for posts created in the last 7 days.
    - Calculate engagement (Score + Num Comments).
    - Sort and pick the top 5 per subreddit.
    - Save the output to `.tmp/reddit_top_posts.json`.
3.  Verify the output file exists and contains data.

## Edge Cases
- **API Limits**: If Reddit blocks the request (429), the script should fail gracefully or wait.
- **Empty Subreddit**: If a subreddit doesn't exist or is empty, log a warning and continue with others.
- **No posts in last week**: If the 100 newest posts are older than 1 week (unlikely for active subs), the result for that sub might be empty.
