#!/usr/bin/python3
"""that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed"""
    headers = {
        'User-agent': 'Holberton',
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url, headers=headers)

    if (req.status_code != 200):
        print(None)
        return

    try:
        childrens = req.json().get('data').get('children')
        for children in childrens:
            print(children.get('data').get('title'))
    except Exception:
        pass
