import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment variables
store_hash = os.getenv('STORE_HASH')
access_token = os.getenv('ACCESS_TOKEN')
client_id = os.getenv('CLIENT_ID')

# Headers for the API request
headers = {
    'X-Auth-Token': access_token,
    'X-Auth-Client': client_id,
    'Content-Type': 'application/json'
}

def get_api_response(url, method='get', json=None):
    """Make an API request and return the response."""
    response = requests.request(method, url, headers=headers, json=json)
    return response


def get_credentials():
    """Return the API credentials."""
    return store_hash, access_token, client_id
