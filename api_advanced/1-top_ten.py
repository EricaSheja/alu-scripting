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
    headers = {"User-Agent": "alu-scripting-app"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data").get("children")

    if not posts:
        print("None")
        return

    for post in posts:
        print(post.get("data").get("title"))
