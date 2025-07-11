import pandas as pd
import numpy as np

# Global list to collect backtest results
results = []

def run_backtest(signal_df, price_data, tickers, alpha_name, holding_period=1):
    for ticker in tickers:
        try:
            signal = signal_df[ticker]
            returns_df = price_data[ticker]['returns']

            aligned = pd.concat([signal, returns_df], axis=1, keys=['signal', 'returns']).dropna()
            signal = aligned['signal']
            returns = aligned['returns']

            position = np.sign(signal.shift(1))
            future_returns = returns.shift(-holding_period)
            strat_returns = position * future_returns

            result_df = pd.DataFrame(index=aligned.index)
            result_df['return'] = strat_returns.fillna(0)
            result_df['cumulative'] = (1 + result_df['return']).cumprod()

            total_return = result_df['cumulative'].iloc[-1] - 1
            max_drawdown = (result_df['cumulative'] / result_df['cumulative'].cummax() - 1).min()
            sharpe_ratio = (
                result_df['return'].mean() / result_df['return'].std() * np.sqrt(252)
                if result_df['return'].std() > 0 else float('nan')
            )

            # Compute custom score
            score = (
                0.5 * sharpe_ratio +
                0.4 * total_return * 100 +
                0.1 * max_drawdown * 100
            )

            # Save results to global list
            results.append({
                'Alpha': alpha_name,
                'Ticker': ticker,
                'Return (%)': total_return * 100,
                'Sharpe': sharpe_ratio,
                'Max Drawdown (%)': max_drawdown * 100,
                'Score': score
            })

        except Exception as e:
            print(f"Backtest failed for {alpha_name} on {ticker}: {e}")

def get_summary():
    return pd.DataFrame(results)
