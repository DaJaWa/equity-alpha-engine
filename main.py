from utils.data_loader import load_equity_data
from alphas.alpha_engine import apply_all_alphas
from backtest.backtester import run_backtest
import pandas as pd

tickers = ["AAPL", "MSFT", "GOOG"]
start_date = "2020-01-01"
end_date = "2023-01-01"

price_data = load_equity_data(tickers, start=start_date, end=end_date)

# Apply and test each alpha independently
for ticker in tickers:
    df = price_data[ticker].copy()
    df['returns'] = df['close'].pct_change()
    signal_df = apply_all_alphas(df)

    for alpha_name in signal_df.columns:
        signal = signal_df[alpha_name].dropna()
        print(f"\n=== {alpha_name} on {ticker} ===")
        run_backtest(signal.to_frame(ticker), price_data, [ticker])
