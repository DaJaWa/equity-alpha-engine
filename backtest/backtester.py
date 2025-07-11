import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_backtest(signal_df, price_data, tickers, holding_period=1):
    """
    Backtest a trading strategy using alpha signals.

    Parameters:
    - signal_df: DataFrame with datetime index and one column per alpha signal
    - price_data: dict of DataFrames keyed by ticker, each with OHLCV + returns
    - tickers: list of tickers to test
    - holding_period: how many days to hold the position
    """
    for ticker in tickers:
        try:
            signal = signal_df[ticker]
            returns_df = price_data[ticker]['returns']

            print(f"\n=== {signal_df.columns[0]} on {ticker} ===")

            # Align and clean
            aligned = pd.concat([signal, returns_df], axis=1, keys=['signal', 'returns']).dropna()
            signal = aligned['signal']
            returns = aligned['returns']

            # Generate position: use previous day's signal
            position = np.sign(signal.shift(1))

            # Apply holding period by forward shifting returns
            future_returns = returns.shift(-holding_period)

            # Calculate strategy returns
            strat_returns = position * future_returns

            # Build result df
            result_df = pd.DataFrame(index=aligned.index)
            result_df['return'] = strat_returns.fillna(0)
            result_df['cumulative'] = (1 + result_df['return']).cumprod()

            # Compute metrics
            total_return = result_df['cumulative'].iloc[-1] - 1
            max_drawdown = (result_df['cumulative'] / result_df['cumulative'].cummax() - 1).min()

            if result_df['return'].std() > 0:
                sharpe_ratio = result_df['return'].mean() / result_df['return'].std() * np.sqrt(252)
            else:
                sharpe_ratio = float('nan')

            # Print results
            print(f"Total Return: {total_return * 100:.2f}%")
            print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
            print(f"Max Drawdown: {max_drawdown * 100:.2f}%")

            # Plot performance
            plt.figure(figsize=(10, 5))
            plt.plot(result_df['cumulative'], label='Cumulative Return')
            plt.title(f"{signal_df.columns[0]} on {ticker}")
            plt.xlabel("Date")
            plt.ylabel("Portfolio Value")
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Backtest failed for {ticker}: {e}")
