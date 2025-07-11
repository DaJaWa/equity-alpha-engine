import pandas as pd
from utils.data_loader import load_equity_data
from backtest.backtester import run_backtest, get_summary

# === Import All Alphas ===
from alphas import (
    alpha_001, alpha_002, alpha_003, alpha_004, alpha_005,
    alpha_006, alpha_007, alpha_008, alpha_009, alpha_010,
    alpha_011, alpha_012, alpha_013, alpha_014, alpha_015,
    alpha_016, alpha_017, alpha_018, alpha_019, alpha_020,
    alpha_101
)

# === Parameters ===
tickers = [
    "AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "META",
    "TSLA", "BRK-B", "JPM", "JNJ", "V", "UNH", "PG",
    "XOM", "MA"
]
start_date = "2020-01-01"
end_date = "2023-01-01"

# === Map Alpha Names to Functions ===
alpha_functions = {
    "alpha_001": alpha_001.alpha_001,
    "alpha_002": alpha_002.alpha_002,
    "alpha_003": alpha_003.alpha_003,
    "alpha_004": alpha_004.alpha_004,
    "alpha_005": alpha_005.alpha_005,
    "alpha_006": alpha_006.alpha_006,
    "alpha_007": alpha_007.alpha_007,
    "alpha_008": alpha_008.alpha_008,
    "alpha_009": alpha_009.alpha_009,
    "alpha_010": alpha_010.alpha_010,
    "alpha_011": alpha_011.alpha_011,
    "alpha_012": alpha_012.alpha_012,
    "alpha_013": alpha_013.alpha_013,
    "alpha_014": alpha_014.alpha_014,
    "alpha_015": alpha_015.alpha_015,
    "alpha_016": alpha_016.alpha_016,
    "alpha_017": alpha_017.alpha_017,
    "alpha_018": alpha_018.alpha_018,
    "alpha_019": alpha_019.alpha_019,
    "alpha_020": alpha_020.alpha_020,
    "alpha_101": alpha_101.alpha_101,
}

# === Load Price Data ===
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# === Run Backtests ===
for alpha_name, alpha_func in alpha_functions.items():
    for ticker in tickers:
        try:
            df = price_data[ticker].copy()
            signal = alpha_func(df)
            run_backtest(signal.to_frame(name=ticker), {ticker: df}, [ticker], alpha_name)
        except Exception as e:
            print(f"Backtest failed for {alpha_name} on {ticker}: {e}")

# === Show Final Summary Table ===
summary_df = get_summary()
print("\n=== Backtest Summary (Ranked by Score) ===")
print(summary_df.sort_values(by="Score", ascending=False))
