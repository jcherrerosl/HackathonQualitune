import os
import requests

client_id = os.getenv("OPEN_GATEWAY_CLIENT_ID")
client_secret = os.getenv("OPEN_GATEWAY_CLIENT_SECRET")
callback_url = os.getenv("OPEN_GATEWAY_CALLBACK_URL")
enduser_id = os.getenv("OPEN_GATEWAY_ENDUSER_ID")

def get_token():
    url = "https://api.dte.open-gateway.dev/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=payload)
    return response.json()["access_token"]

def verify_number(phone):
    token = get_token()
    url = "https://api.dte.open-gateway.dev/dpv/number-verification/v1/verify"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-end-user-id": enduser_id,
    }
    data = {
        "phoneNumber": phone
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def verify_identity(full_name):
    token = get_token()
    url = "https://api.dte.open-gateway.dev/dpv/kyc-match/v1/match"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-end-user-id": enduser_id,
    }
    data = {
        "fullName": full_name
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
