import json
import requests


def quote():
    res = requests.get("http://quotes.rest/qod.json?category=inspire").json()
    quote = res["contents"]["quotes"][0]
    return quote


globals = {"quote": quote}
