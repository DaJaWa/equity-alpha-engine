import yfinance as yf
import pandas as pd
import os

def load_equity_data(tickers, start="2020-01-01", end="2023-01-01"):
    """
    Load OHLCV data for a list of tickers using yfinance.

    Returns:
        dict of DataFrames keyed by ticker
    """
    print(f"Downloading data for: {', '.join(tickers)}")
    raw_data = yf.download(tickers, start=start, end=end, group_by="ticker", auto_adjust=True)

    data_dict = {}
    for ticker in tickers:
        df = raw_data[ticker][['Open', 'High', 'Low', 'Close', 'Volume']].copy()
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df['returns'] = df['close'].pct_change()
        df['vwap'] = (df['high'] + df['low'] + df['close']) / 3
        df['adv20'] = df['volume'].rolling(window=20).mean()
        data_dict[ticker] = df.dropna()

    return data_dict
