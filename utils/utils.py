# utils.py
import requests
import pickle
import math
from sklearn.linear_model import LinearRegression
from tensorflow import keras

def fetch_data():
    # Define API endpoint and parameters
    endpoint = "https://api.chia-network.com/get_network_info"
    params = {"key": "your_api_key"}

    # Send GET request to API and parse response
    response = requests.get(endpoint, params=params)
    data = response.json()

    return data

def process_data(historical_data, chia_network_data, market_data):
    # Calculate average price of historical data
    total_price = 0
    for data_point in historical_data:
        total_price += data_point["price"]
    average_price = total_price / len(historical_data)

    # Check if Chia network is stable
    if chia_network_data["status"] == "stable":
        print("Chia network is stable")
    else:
        print("Chia network is not stable")

    # Determine if market is bullish or bearish
    if market_data["trend"] == "bullish":
        print("Market is currently bullish")
    elif market_data["trend"] == "bearish":
        print("Market is currently bearish")
    else:
        print("Market trend is uncertain")

def train_model(processed_data):
    # Define features and labels
    X = processed_data["features"]
    y = processed_data["labels"]

    # Initialize LinearRegression model and fit to data
    model = LinearRegression()
    model.fit(X, y)

    return model

def save_model(model, file_path):
    # Save model to disk using pickle
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

def load_model(file_path):
    # Load model from HDF5 file
    model = keras.models.load_model(file_path)
    return model

