from utils.data_loader import load_equity_data
from backtest.backtester import run_backtest
import pandas as pd
import importlib

# === Configuration ===
tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

# === Load historical price data ===
print(f"\nDownloading data for: {', '.join(tickers)}")
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Add returns to each ticker's data
for ticker in tickers:
    df = price_data[ticker]
    df['returns'] = df['close'].pct_change()
    price_data[ticker] = df.dropna()

# === List of alpha functions to test ===
alpha_list = [
    "alpha_001",
    "alpha_002",
    "alpha_003",
    "alpha_004",
    "alpha_005",
    "alpha_101"
]

# === Run each alpha strategy ===
for alpha_name in alpha_list:
    try:
        module = importlib.import_module(f"alphas.{alpha_name}")
        alpha_func = getattr(module, alpha_name)

        signal_df = pd.DataFrame()

        for ticker in tickers:
            df = price_data[ticker].copy()
            signal = alpha_func(df)
            signal.name = ticker
            signal_df[ticker] = signal

        run_backtest(signal_df, price_data, tickers)

    except Exception as e:
        print(f"\nError processing {alpha_name}: {e}")
