# main.py

import chia_network
import market_data
import data_processing
from utils import *

if __name__ == "__main__":
    # Load historical data
    historical_data = data_processing.load_data("data/historical_data.csv")

    # Fetch Chia network data
    chia_network_data = chia_network.fetch_data()

    # Fetch market data
    market_data = market_data.fetch_data()

    # Process and analyze data
    processed_data = data_processing.process_data(historical_data, chia_network_data, market_data)

    # Train machine learning model
    model = data_processing.train_model(processed_data)

    # Save trained model
    data_processing.save_model(model, "models/chia_tracker_model.h5")
