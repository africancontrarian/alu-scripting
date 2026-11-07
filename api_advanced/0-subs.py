#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a subreddit.

    Return 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        data = response.json().get("data") or {}
    except ValueError:
        return 0
    return data.get("subscribers") or 0
