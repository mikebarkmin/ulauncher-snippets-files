import json
import re
from typing import Dict
import dotenv
import requests
import urllib.request
import json
import urllib
import tweepy
import os
from bs4 import BeautifulSoup


def random_image(dimension="1200x400"):
    res = requests.get(f"https://source.unsplash.com/random/{dimension}")
    return res.url


def quote():
    res = requests.get("http://quotes.rest/qod.json?category=inspire").json()
    quote = res["contents"]["quotes"][0]
    return quote


cached_youtube_infos: Dict[str, str] = {}


def youtube_info(url: str):
    params = {"format": "json", "url": url}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    cached_info = cached_youtube_infos.get(url)
    if not cached_info:
        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            cached_youtube_infos[url] = data
            return data
    else:
        return cached_info


cached_twitter_infos: Dict[str, str] = {}


def twitter_info(url: str):
    """
    >>> twitter_info('https://twitter.com/ACMDL/status/1426961667892596738')['author_name']
    'ACM Digital Library'
    """
    params = {"url": url}
    url = "https://publish.twitter.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    cached_info = cached_twitter_infos.get(url)
    if not cached_info:
        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            clean_text = " ".join(
                BeautifulSoup(data["html"], "html.parser").stripped_strings
            )
            data["title"] = clean_text[:40]
            cached_twitter_infos[url] = data

            return data
    else:
        return cached_info


globals = {
    "quote": quote,
    "random_image": random_image,
    "youtube_info": youtube_info,
    "twitter_info": twitter_info
}

if __name__ == "__main__":
    import doctest
    from freezegun import freeze_time

    freezer = freeze_time("2020-12-10 12:00:01")
    freezer.start()
    doctest.testmod()
    freezer.stop()
