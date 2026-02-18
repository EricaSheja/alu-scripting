#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a subreddit.
    If the subreddit is invalid, prints None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:reddit.api.project:v1.0 (by /u/yourusername)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False  # Prevent following redirects
        )

        # If subreddit is invalid (404) or redirect (302), print None
        if response.status_code != 200:
            print(None)
            return

        data = response.json()

        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
