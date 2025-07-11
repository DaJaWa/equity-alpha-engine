import pandas as pd
from utils.data_loader import load_equity_data
from backtest.backtester import run_backtest
from alphas.alpha_001 import alpha_001
from alphas.alpha_002 import alpha_002
from alphas.alpha_003 import alpha_003
from alphas.alpha_004 import alpha_004
from alphas.alpha_005 import alpha_005
from alphas.alpha_101 import alpha_101

# List of tickers and date range
tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

# Load historical price data
print(f"Downloading data for: {', '.join(tickers)}")
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Determine if price_data is a dict or DataFrame
is_dict = isinstance(price_data, dict)

# Dictionary of alpha functions to test
alpha_functions = {
    "alpha_001": alpha_001,
    "alpha_002": alpha_002,
    "alpha_003": alpha_003,
    "alpha_004": alpha_004,
    "alpha_005": alpha_005,
    "alpha_101": alpha_101,
}

# Store results
results_summary = []

# Run each alpha on each ticker
for alpha_name, alpha_func in alpha_functions.items():
    print(f"\n=== {alpha_name} ===")
    for ticker in tickers:
        print(f"\n--- {ticker} on {ticker} ---")
        try:
            # Extract the dataframe for the specific ticker
            df = price_data[ticker].copy() if is_dict else price_data[price_data["ticker"] == ticker].copy()

            # Ensure datetime index
            df.index = pd.to_datetime(df.index)

            # Generate alpha signal
            signal = alpha_func(df)

            # Run backtest
            result = run_backtest(signal.to_frame(name=alpha_name), price_data, [ticker])
            if result:
                result["alpha"] = alpha_name
                result["ticker"] = ticker
                results_summary.append(result)
        except Exception as e:
            print(f"Backtest failed for {ticker}: {e}")

# Save results if any
if results_summary:
    summary_df = pd.DataFrame(results_summary)
    summary_df.to_csv("backtest_results_summary.csv", index=False)
    print("\nAll backtests completed. Summary saved to 'backtest_results_summary.csv'.")
else:
    print("\nNo valid backtest results to save.")
