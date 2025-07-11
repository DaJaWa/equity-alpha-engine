def alpha_018(df):
    """
    Alpha 018: -1 * rank(stddev(close, 5) + mean(close, 20))
    """
    try:
        import pandas as pd

        std_5 = df['close'].rolling(5).std()
        mean_20 = df['close'].rolling(20).mean()
        combined = std_5 + mean_20
        result = -1 * combined.rank()

        return result
    except Exception as e:
        print(f"Error in alpha_018: {e}")
        return df['close'] * 0
