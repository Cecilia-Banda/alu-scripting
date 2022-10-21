#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests
import sys
import json


def number_of_subscribers(subreddit):
    """get all subscribers"""
    if len(sys.argv) < 2:
        return 0
    else:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = requests.get(url, headers=headers, allow_redirects=False)
        if result.status_code != 200:
            return 0
        body = json.loads(result.text)
        return body["data"]["subscribers"]
