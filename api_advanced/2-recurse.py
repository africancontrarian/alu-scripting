#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def recurse(subreddit, hot_list=None, after=None):
    """Return a list with the titles of all hot posts of a subreddit.

    Follow the pagination of the Reddit API recursively through the
    `after` token. Return None if the subreddit is invalid or has no posts.
    """
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return hot_list if hot_list else None
    try:
        data = response.json().get("data") or {}
    except ValueError:
        return hot_list if hot_list else None
    for post in data.get("children") or []:
        hot_list.append((post.get("data") or {}).get("title"))
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
