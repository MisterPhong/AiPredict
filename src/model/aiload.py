import numpy as np
import pandas as pd
from binance.client import Client
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

# Load the model
model = load_model('crypto_price_prediction_model.h5')

# Function to get crypto data from Binance API
def get_crypto_data(coin_symbol, interval='1d', limit=365):
    api_key = 'dhxyexgq56p8qfXIXdkL40DOTfpopgBysz8IEbvxJfuqksbDphNubGS8ydMFJTAI'
    api_secret = 'nquFquj6eKLmvgWJ4Er6SlFYFte8b0auIKfFmKUH0A7Fh6Mg7FGKb97PPgZggXnO'
    client = Client(api_key, api_secret)

    interval_map = {
        '1d': Client.KLINE_INTERVAL_1DAY,
        '1h': Client.KLINE_INTERVAL_1HOUR,
        '1m': Client.KLINE_INTERVAL_1MINUTE
    }
    
    interval = interval_map.get(interval)
    if not interval:
        raise ValueError("Invalid interval. Use '1d', '1h', or '1m'.")

    klines = client.get_historical_klines(coin_symbol, interval, f"{limit} day ago UTC")
    timestamps = [datetime.utcfromtimestamp(kline[0] / 1000) for kline in klines]
    prices = [float(kline[4]) for kline in klines]
    df = pd.DataFrame({'timestamp': timestamps, 'price': prices})
    return df

# Function to preprocess data and add EMA values
def preprocess_data(data, ema_period=20):
    data['price_ema'] = data['price'].ewm(span=ema_period, adjust=False).mean()
    return data[['timestamp', 'price', 'price_ema']]

# List of coin symbols
coin_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT', 'XRPUSDT',
                'DOTUSDT', 'SOLUSDT', 'DOGEUSDT', 'LTCUSDT', 'LINKUSDT',
                'MATICUSDT', 'UNIUSDT', 'ICPUSDT', 'VETUSDT', 'XLMUSDT',
                'FILUSDT', 'TRXUSDT', 'AAVEUSDT', 'EOSUSDT', 'THETAUSDT']

results = []

for symbol in coin_symbols:
    # Fetch data for the coin symbol
    crypto_data = get_crypto_data(symbol, interval='1d', limit=365)
    crypto_data = preprocess_data(crypto_data, ema_period=20)
    
    # Select features for prediction
    prediction_data = crypto_data[['price', 'price_ema']]
    
    # Normalize/Scale the input features
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(prediction_data)
    
    # Create a separate scaler for the target variable (price)
    price_scaler = MinMaxScaler()
    price_scaler.fit(prediction_data[['price']])
    
    # Prepare data for prediction (use the last 30 days of the scaled data)
    time_step = 30
    last_30_days_scaled = scaled_data[-time_step:]
    X_future = np.expand_dims(last_30_days_scaled, axis=0)
    
    # Make predictions
    predictions = model.predict(X_future)
    
    # Inverse scale the predictions using the target variable scaler
    predicted_price = price_scaler.inverse_transform(predictions)

    # Fetch actual price for the next day
    next_day_timestamp = crypto_data['timestamp'].iloc[-1] + timedelta(days=1)
    actual_price_data = get_crypto_data(symbol, interval='1d', limit=2)
    actual_price = actual_price_data[actual_price_data['timestamp'] == next_day_timestamp]['price'].values
    if len(actual_price) > 0:
         actual_price = actual_price[0]
    else:
        actual_price = np.nan  # In case the actual price is not available
    
    # Prepare the result
    last_timestamp = crypto_data['timestamp'].iloc[-1]
    next_day = last_timestamp + timedelta(days=1)
    current_price = crypto_data['price'].iloc[-1]
    
    current_time = datetime.utcnow()
    
    result = {
        'Symbol': symbol,
        'Date': next_day,
        'Time': next_day.strftime('%H:%M:%S'),
        'Current Price': current_price,
        'Predicted Price': predicted_price.flatten()[0],
        'Actual Price': actual_price,
        'createdAt': current_time,
        'updatedAt': current_time
    }
    
    results.append(result)


# Convert results to DataFrame
result_df = pd.DataFrame(results)

# Set display options to show full columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Print detailed results for each symbol
for index, row in result_df.iterrows():
    print(f"--- {row['Symbol']} ---")
    print(f"Date: {row['Date'].date()}")
    print(f"Time: {row['Time']}")
    print(f"Current Price: {row['Current Price']:.2f}")
    print(f"Predicted Price: {row['Predicted Price']:.2f}")
    print(f"Actual Price: {row['Actual Price']:.2f}")
    print(f"createdAt: {row['createdAt']}")
    print(f"updatedAt: {row['updatedAt']}")
    print("--------------------------------")
    
print(result_df)
