#!/usr/bin/python3
"""Recursively count keywords in the titles of the hot posts of a subreddit."""
import requests

USER_AGENT = "python:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def print_counts(counts, word_list):
    """Print the keyword counts, sorted by count then alphabetically.

    Duplicated keywords in word_list (case-insensitive) add up, and
    keywords without any match are skipped.
    """
    words = [word.lower() for word in word_list]
    totals = {}
    for word in set(words):
        total = counts.get(word, 0) * words.count(word)
        if total:
            totals[word] = total
    for word, total in sorted(totals.items(),
                              key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Follow the pagination of the Reddit API recursively through the
    `after` token. Print nothing if the subreddit is invalid or if no
    title contains a keyword.
    """
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print_counts(counts, word_list)
        return
    try:
        data = response.json().get("data") or {}
    except ValueError:
        print_counts(counts, word_list)
        return
    wanted = set(word.lower() for word in word_list)
    for post in data.get("children") or []:
        title = (post.get("data") or {}).get("title") or ""
        for token in title.lower().split():
            if token in wanted:
                counts[token] = counts.get(token, 0) + 1
    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_counts(counts, word_list)
