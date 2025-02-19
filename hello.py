from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api.bitfinex.com/v2"

API_KEY, API_SECRET = (
    "2441ccef40f982f4774ebaa0a9c31fe099d6c2df720",
    "f67ba3583479926379c05a0184596456603857ccd71"
)

# Endpoint for getting available funds for funding
endpoint_funding = "auth/calc/order/avail"
# Endpoint for submit a new funding offer.
credit_funding = "auth/r/funding/credits/fEUR"

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
  
endpoint = endpoint_funding
endpoint_2 = credit_funding

payload = {
    "symbol": "fEUR",
    "type": "FUNDING",
}

payload_2 = {}

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    **_build_authentication_headers(endpoint, payload)
}

response = requests.post(f"{API}/{endpoint}", json=payload, headers=headers)

headers_2 = {
    "accept": "application/json",
    "Content-Type": "application/json",
    **_build_authentication_headers(endpoint_2, payload_2)
}

response_credit_funding = requests.post(f"{API}/{endpoint_2}", json=payload_2, headers=headers_2)

print(response.json())
print(response_credit_funding.json())
