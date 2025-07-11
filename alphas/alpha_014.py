def alpha_014(df):
    """
    Alpha 014: -1 * rank(delta(return, 3)) * correlation(open, volume, 10)
    """
    try:
        import pandas as pd

        delta_return = df['returns'].diff(3)
        ranked_delta = delta_return.rank()
        corr = df['open'].rolling(10).corr(df['volume'])

        result = -1 * ranked_delta * corr
        return result
    except Exception as e:
        print(f"Error in alpha_014: {e}")
        return df['close'] * 0
