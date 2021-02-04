#!/usr/bin/python3

'''
    consulta de de numeros de supscritores
    en Reddit(activos y supscriptores totales)
'''
import requests


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given"""
    headers = {
        'User-agent': 'Holberton'
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers)

    try:
        return req.json().get("data").get("subscribers")
    except Exception:
        return 0
