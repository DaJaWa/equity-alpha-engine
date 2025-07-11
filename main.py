import pandas as pd
from utils.data_loader import load_equity_data
from backtest.backtester import run_backtest

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
    "AAPL", "MSFT", "GOOG", "AMZN", "META",
    "NVDA", "TSLA", "UNH", "JPM", "V",
    "JNJ", "HD", "MA", "PG", "AVGO"
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

# === Collect Results ===
results = []

# === Loop Through Alphas ===
for alpha_name, alpha_func in alpha_functions.items():
    for ticker in tickers:
        try:
            df = price_data[ticker].copy()
            signal = alpha_func(df)
            metrics = run_backtest(signal.to_frame(name=ticker), {ticker: df}, [ticker])
            results.append({
                "Alpha": alpha_name,
                "Ticker": ticker,
                "Return (%)": round(metrics["total_return"] * 100, 2),
                "Sharpe": round(metrics["sharpe_ratio"], 2),
                "Max Drawdown (%)": round(metrics["max_drawdown"] * 100, 2),
            })
        except Exception as e:
            results.append({
                "Alpha": alpha_name,
                "Ticker": ticker,
                "Return (%)": "ERR",
                "Sharpe": "ERR",
                "Max Drawdown (%)": "ERR",
            })
            print(f"Backtest failed for {ticker} with {alpha_name}: {e}")

# === Display Summary Table ===
summary_df = pd.DataFrame(results)
print("\n=== Backtest Summary ===")
print(summary_df.to_string(index=False))
