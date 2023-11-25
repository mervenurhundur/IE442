import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = 'https://www.alphavantage.co/query'

# API key
api_key = 'UU6KXGB8ZSOMM7EK'
symbol = 'IBM'
function = 'TIME_SERIES_INTRADAY'
datatype = 'json'
interval = '60min'  # Saatte bir veri almak için 60 dakikalık interval
outputsize = 'compact'  # ilk 100 veriyi almak için

params = {
    "function": function,
    "apikey": api_key,
    "symbol": symbol,
    'datatype': datatype,
    'interval': interval,
    'outputsize': outputsize,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Parse the JSON data into objects
    results = data.get("Time Series (60min)", {})
    timeline = []

    for date, values in results.items():
        company_name = symbol
        company_stock = float(values.get("4. close", 0))  # Assuming "4. close" contains the stock value
        timeline.append({
            "date": date,
            "name": company_name,
            "stock": company_stock,
        })

    # Sort the timeline by date
    timeline = sorted(timeline, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))

    # Extract dates and stocks for plotting
    dates = [entry['date'] for entry in timeline]
    stocks = [entry['stock'] for entry in timeline]

    # Plot the data
    plt.plot(dates, stocks, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(f'Hourly Stock Values for {symbol}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

else:
    print('Request failed. Error code:', response.status_code)
