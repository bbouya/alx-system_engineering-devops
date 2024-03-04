#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import json
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates success
    if response.status_code != 200:
        print("Subreddit not found or unavailable.")
        return

    # Attempt to parse the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return

    # Check if 'data' key exists in the JSON response
    if 'data' not in data or 'children' not in data['data']:
        print("No data found in response.")
        return

    # Extract the 'data' section
    results = data['data']

    # Print the titles of the top 10 hottest posts
    for post in results['children']:
        print(post.get("data").get("title"))
