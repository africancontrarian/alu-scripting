#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests
import sys

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def safe_print(text):
    """Print text, falling back to UTF-8 bytes on non UTF-8 terminals."""
    try:
        print(text)
    except UnicodeEncodeError:
        sys.stdout.flush()
        sys.stdout.buffer.write((str(text) + "\n").encode("utf-8"))
        sys.stdout.flush()


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        children = response.json().get("data").get("children")
    except (AttributeError, ValueError):
        print(None)
        return
    if not children:
        print(None)
        return
    for post in children[:10]:
        safe_print(post.get("data").get("title"))
