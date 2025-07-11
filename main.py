from utils.data_loader import load_equity_data
from alphas.alpha_engine import apply_all_alphas
from backtest.backtester import run_backtest
import pandas as pd

# Define tickers and date range
tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

# Load OHLCV data
price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Storage for per-alpha performance
all_alpha_results = {}

# Loop through all tickers and apply all alphas
for ticker in tickers:
    df = price_data[ticker]
    all_signals = apply_all_alphas(df)

    # Run backtest for each alpha independently
    for alpha_name in all_signals.columns:
        signal_series = all_signals[alpha_name].dropna()
        signal_df = pd.DataFrame({ticker: signal_series})

        print(f"\n=== Running backtest for {alpha_name} on {ticker} ===")
        run_backtest(signal_df, price_data, [ticker])
