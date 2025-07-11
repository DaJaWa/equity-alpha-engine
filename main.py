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

# Load data
print(f"Downloading data for: {', '.join(tickers)}")
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Detect if the loader returned a dict or DataFrame
is_dict = isinstance(price_data, dict)

# Define alphas
alpha_functions = {
    "alpha_001": alpha_001,
    "alpha_002": alpha_002,
    "alpha_003": alpha_003,
    "alpha_004": alpha_004,
    "alpha_005": alpha_005,
    "alpha_101": alpha_101,
}

# Loop through each alpha and ticker
for alpha_name, alpha_func in alpha_functions.items():
    print(f"\n=== {alpha_name} ===")
    for ticker in tickers:
        print(f"\n--- {ticker} on {ticker} ---")
        try:
            # Get data for ticker
            if is_dict:
                df = price_data[ticker].copy()
            else:
                df = price_data[price_data["ticker"] == ticker].copy()

            df.index = pd.to_datetime(df.index)

            # Generate alpha signal
            signal = alpha_func(df)

            # Run backtest
            if is_dict:
                run_backtest(signal.to_frame(name=alpha_name), {ticker: df}, [ticker])
            else:
                run_backtest(signal.to_frame(name=alpha_name), df, [ticker])

        except Exception as e:
            print(f"Backtest failed for {ticker}: {e}")
