from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api.bitfinex.com/v2"

API_KEY, API_SECRET = (
    "2441ccef40f982f4774ebaa0a9c31fe099d6c2df720",
    "f67ba3583479926379c05a0184596456603857ccd71"
)

stats = "https://api-pub.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/hist"

headers = {"accept": "application/json"}

response = requests.get(stats, headers=headers)

print(response.text)