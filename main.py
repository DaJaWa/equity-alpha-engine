from utils.data_loader import load_equity_data
from alphas.alpha_101 import alpha_101
from backtest.backtester import run_backtest
import pandas as pd

# Define tickers to test
tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

# Load data
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Compute alpha signals
alpha_signals = {}
for ticker in tickers:
    df = price_data[ticker].copy()
    alpha_signals[ticker] = alpha_101(df)

# Combine signals into a DataFrame
signal_df = pd.DataFrame(alpha_signals)

# Run backtest
run_backtest(signal_df, price_data, tickers)
