from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api.bitfinex.com/v2"

API_KEY, API_SECRET = (
    "2441ccef40f982f4774ebaa0a9c31fe099d6c2df720",
    "f67ba3583479926379c05a0184596456603857ccd71"
)

movements = "https://api.bitfinex.com/v2/auth/r/movements/Currency/hist"

def _build_authentication_headers(endpoint, payload = None):
    nonce = str(round(datetime.now().timestamp() * 1_000))

    message = f"/api/v2/{endpoint}{nonce}"

    if payload != None:
        message += json.dumps(payload)

    signature = hmac.new(
        key=API_SECRET.encode("utf8"),
        msg=message.encode("utf8"),
        digestmod=hashlib.sha384
    ).hexdigest()

    return {
        "bfx-apikey": API_KEY,
        "bfx-nonce": nonce,
        "bfx-signature": signature
    }


headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(movements, headers=headers)

print(response.text)