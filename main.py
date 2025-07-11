import pandas as pd
from utils.data_loader import load_equity_data
from backtest.backtester import run_backtest
from alphas.alpha_001 import alpha_001
from alphas.alpha_002 import alpha_002
from alphas.alpha_003 import alpha_003
from alphas.alpha_004 import alpha_004
from alphas.alpha_005 import alpha_005
from alphas.alpha_101 import alpha_101

# Define parameters
tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

# Load price data
print(f"Downloading data for: {', '.join(tickers)}")
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Check if data is dict (YahooFinance version returns dict)
is_dict = isinstance(price_data, dict)

# Define alphas to test
alpha_functions = {
    "alpha_001": alpha_001,
    "alpha_002": alpha_002,
    "alpha_003": alpha_003,
    "alpha_004": alpha_004,
    "alpha_005": alpha_005,
    "alpha_101": alpha_101,
}

# Run each alpha on each ticker
for alpha_name, alpha_func in alpha_functions.items():
    print(f"\n=== {alpha_name} ===")
    for ticker in tickers:
        print(f"\n--- {ticker} on {ticker} ---")
        try:
            # Slice the correct format of price data
            df = price_data[ticker].copy() if is_dict else price_data[price_data['ticker'] == ticker].copy()
            df.index = pd.to_datetime(df.index)

            # Generate alpha signal
            signal = alpha_func(df)

            # Run backtest with the correct sub-data
            price_subset = {ticker: df} if is_dict else df
            run_backtest(signal.to_frame(name=alpha_name), price_subset, [ticker])

        except Exception as e:
            print(f"Backtest failed for {ticker}: {e}")
