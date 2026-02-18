#!/usr/bin/python3
"""
1-top_ten
Prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print top 10 hot post titles of a subreddit."""
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "alu-scripting"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data").get("children")
    except Exception:
        print("None")
        return

    if posts is None:
        print("None")
        return

    for post in posts[:10]:
        print(post.get("data").get("title"))
