def alpha_017(df):
    """
    Alpha 017: -1 * rank(stddev(close, 20))
    """
    try:
        import pandas as pd

        rolling_std = df['close'].rolling(20).std()
        ranked_std = rolling_std.rank()
        result = -1 * ranked_std
        return result
    except Exception as e:
        print(f"Error in alpha_017: {e}")
        return df['close'] * 0
