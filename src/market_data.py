# market_data.py

import requests

response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chia&vs_currencies=usd')

if response.status_code == 200:
    chia_price = response.json()['chia']['usd']
    print(f"1 Chia = {chia_price} EUR = {chia_price} USD = {chia_price}")
else:
    print(f"Error: {response.status_code}")
