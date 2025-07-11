def alpha_016(df):
    """
    Alpha 016: -1 * rank(correlation(open, volume, 10))
    """
    try:
        import pandas as pd

        corr = df['open'].rolling(10).corr(df['volume'])
        ranked_corr = corr.rank()
        result = -1 * ranked_corr
        return result
    except Exception as e:
        print(f"Error in alpha_016: {e}")
        return df['close'] * 0
