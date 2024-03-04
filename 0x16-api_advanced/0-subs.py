#!/usr/bin/python3
"""this module contain function to fetch data from reddit api"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.


    Arguments:
      subreddit : string contain the name of redit topic

    Return:
      n : the number of subscribers (not active users, total subscribers)
      for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]

    return 0
