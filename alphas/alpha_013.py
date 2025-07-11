def alpha_013(df):
    """
    Alpha 013: -1 * rank(covariance(rank(close), rank(volume), 5))
    """
    try:
        import pandas as pd

        ranked_close = df['close'].rank()
        ranked_volume = df['volume'].rank()

        cov = ranked_close.rolling(5).cov(ranked_volume)
        result = -1 * cov.rank()

        return result
    except Exception as e:
        print(f"Error in alpha_013: {e}")
        return df['close'] * 0
