#!/usr/bin/python3
"""
number of subscribers for a given subreddit
using reddit api else if invalid let it return zero
"""
from request import get


def number_of_subscribers(subreddit):
    """
    Function that queries the reddit api and returns 
    the number of subscribers
    for a given sub reddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {"User-agent": "Google Chrome Version 90.0.4199.129"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, headers=user_agent)
    result = response.json()

    try:
        return results.get("data").get("subscribers")

    except Exception:
        return 0
