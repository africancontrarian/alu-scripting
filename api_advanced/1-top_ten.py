#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        data = response.json().get("data") or {}
    except ValueError:
        print(None)
        return
    for post in (data.get("children") or [])[:10]:
        print((post.get("data") or {}).get("title"))
