# chia_network.py

import requests

def fetch_data():
    # Define API endpoint and parameters
    endpoint = "https://api.chia-network.com/get_network_info"
    params = {"key": "your_api_key"}

    # Send GET request to API and parse response
    response = requests.get(endpoint, params=params)
    data = response.json()

    return data
