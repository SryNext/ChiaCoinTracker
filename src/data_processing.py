# data_processing.py
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import pickle

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            date = row[0]
            price = float(row[1])
            data.append((date, price))
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
