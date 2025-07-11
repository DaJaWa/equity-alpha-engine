import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_backtest(signal_df, price_data, tickers, top_n=1, bottom_n=1, holding_period=1):
    """
    Run a simple long-short backtest using alpha signals.

    Parameters:
        signal_df: DataFrame of signals (tickers as columns)
        price_data: dict of price DataFrames per ticker
        tickers: list of tickers
        top_n: number of long positions
        bottom_n: number of short positions
        holding_period: how long to hold positions (in days)
    """
    signal_df = signal_df.dropna()
    signal_df = signal_df.rank(axis=1)  # cross-sectional ranking

    returns_df = pd.DataFrame(index=signal_df.index)

    for ticker in tickers:
        returns_df[ticker] = price_data[ticker]['returns'].reindex(signal_df.index)

    portfolio_returns = []

    for date in signal_df.index[:-holding_period]:
        scores = signal_df.loc[date]
        longs = scores.nlargest(top_n).index
        shorts = scores.nsmallest(bottom_n).index

        future_returns = returns_df.shift(-holding_period).loc[date]
        long_return = future_returns[longs].mean()
        short_return = future_returns[shorts].mean()

        daily_return = long_return - short_return
        portfolio_returns.append((date, daily_return))

    # Create DataFrame of returns
    result_df = pd.DataFrame(portfolio_returns, columns=["date", "return"]).set_index("date")
    result_df['cumulative'] = (1 + result_df['return']).cumprod()

    # Plot
    result_df['cumulative'].plot(title="Backtest Equity Curve", figsize=(10, 5))
    plt.grid(True)
    plt.ylabel("Cumulative Return")
    plt.xlabel("Date")
    plt.show()

    # Stats
    print("\nBacktest Summary:")
    print(f"Total Return: {result_df['cumulative'].iloc[-1] - 1:.2%}")
    print(f"Sharpe Ratio: {result_df['return'].mean() / result_df['return'].std() * np.sqrt(252):.2f}")
    print(f"Max Drawdown: {(result_df['cumulative'].cummax() - result_df['cumulative']).max():.2%}")
