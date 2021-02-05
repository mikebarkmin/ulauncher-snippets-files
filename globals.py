import json
import requests

def random_image(dimension = "1200x400"):
    res = requests.get(f"https://source.unsplash.com/random/{dimension}")
    return res.url

def quote():
    res = requests.get("http://quotes.rest/qod.json?category=inspire").json()
    quote = res["contents"]["quotes"][0]
    return quote


globals = {"quote": quote, "random_image": random_image}
