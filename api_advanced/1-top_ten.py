#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code in range(300, 600):
        print(None)
        return
    try:
        posts = response.json().get("data").get("children")
    except (AttributeError, ValueError):
        posts = None
    if posts is None:
        print(None)
        return
    for post in posts[:10]:
        print((post.get("data") or {}).get("title"))
