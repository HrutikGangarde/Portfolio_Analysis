# portfolio_analysis.py

import pandas as pd
import yfinance as yf
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt

cg = CoinGeckoAPI()

# Step 1: Input Portfolio Data
stocks = {
    'Ticker': ['RELIANCE.NS', 'TCS.NS', 'INFY.NS'],
    'Quantity': [10, 5, 8],
    'Buy Price': [2500, 3500, 1500]
}

cryptos = {
    'Name': ['bitcoin', 'ethereum'],
    'Quantity': [0.1, 0.5],
    'Buy Price': [2500000, 150000]
}

# Convert to DataFrame
stock_df = pd.DataFrame(stocks)
crypto_df = pd.DataFrame(cryptos)

# Step 2: Fetch Live Prices
stock_df['Current Price'] = [yf.Ticker(ticker).info['regularMarketPrice'] for ticker in stock_df['Ticker']]
crypto_df['Current Price'] = [cg.get_price(ids=name, vs_currencies='inr')[name]['inr'] for name in crypto_df['Name']]

# Step 3: Calculate Portfolio Value and Profit/Loss
stock_df['Current Value'] = stock_df['Quantity'] * stock_df['Current Price']
stock_df['Profit/Loss'] = (stock_df['Current Price'] - stock_df['Buy Price']) * stock_df['Quantity']

crypto_df['Current Value'] = crypto_df['Quantity'] * crypto_df['Current Price']
crypto_df['Profit/Loss'] = (crypto_df['Current Price'] - crypto_df['Buy Price']) * crypto_df['Quantity']

# Step 4: Display Portfolio Summary
print("Stock Portfolio:")
print(stock_df)
print("\nCrypto Portfolio:")
print(crypto_df)

# Step 5: Plot Portfolio Distribution
total_value = stock_df['Current Value'].sum() + crypto_df['Current Value'].sum()
labels = ['Stocks', 'Cryptocurrencies']
sizes = [stock_df['Current Value'].sum(), crypto_df['Current Value'].sum()]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#66b3ff','#ff9999'])
plt.title('Portfolio Distribution')
plt.show()
