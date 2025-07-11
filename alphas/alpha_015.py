def alpha_015(df):
    """
    Alpha 015: -1 * rank(close - vwap) * abs(correlation(close, adv20, 20))
    """
    try:
        import pandas as pd
        import numpy as np

        close_minus_vwap = df['close'] - df['vwap']
        ranked_diff = close_minus_vwap.rank()
        corr = df['close'].rolling(20).corr(df['adv20'])
        result = -1 * ranked_diff * np.abs(corr)
        return result
    except Exception as e:
        print(f"Error in alpha_015: {e}")
        return df['close'] * 0
