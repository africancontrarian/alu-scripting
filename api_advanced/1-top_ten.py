#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                             "alu.api_advanced/1.0 (by /u/alu_student)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        children = response.json().get("data").get("children")
        titles = [child.get("data").get("title") for child in children]
    except Exception:
        titles = []
    if not titles:
        print(None)
        return
    for title in titles[:10]:
        try:
            print(title)
        except UnicodeEncodeError:
            print(title.encode("ascii", "replace").decode("ascii"))
