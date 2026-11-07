# API advanced

Python functions that use the [Reddit API](https://www.reddit.com/dev/api/)
to read subreddit data, handle pagination and parse JSON results.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- The `requests` module (used for every HTTP request)
- Code follows the `PEP 8` style (`pycodestyle`)
- All files are executable and start with `#!/usr/bin/python3`
- Redirects are never followed (invalid subreddits redirect to a search page)
- A custom `User-Agent` is sent with every request

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-subs.py` | `number_of_subscribers(subreddit)` returns the total subscribers, or 0 if the subreddit is invalid |
| 1 | `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` if invalid |
| 2 | `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` recursively returns the titles of all hot posts, or `None` |
| 3 | `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords in hot post titles and prints them sorted |

## Usage

```
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

For task 3, keywords are matched case-insensitively as whole space-delimited
words (`java.`, `java!` and `java_` do not count as `java`). Duplicate keywords
are added together. Results are printed in lowercase, by descending count and
then alphabetically, and keywords without a match are skipped.
