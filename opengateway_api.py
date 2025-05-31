import requests
import os

BASE_URL = "https://opengateway.telefonica.com"
TOKEN_URL = BASE_URL + "/auth/v1/token"
NUMBER_VERIFICATION_URL = BASE_URL + "/dpv/number-verification/verify"
KYC_MATCH_URL = BASE_URL + "/dpv/kyc-match/match"

CLIENT_ID = os.getenv("OPEN_GATEWAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("OPEN_GATEWAY_CLIENT_SECRET")

def get_access_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "dpv:ResearchAndDevelopment#kyc-match:match dpv:ResearchAndDevelopment#number-verification:verify"
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def verify_number(phone_number):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"phoneNumber": phone_number}

    response = requests.post(NUMBER_VERIFICATION_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def verify_identity(full_name):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"fullName": full_name}

    response = requests.post(KYC_MATCH_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
