def alpha_010(df):
    """
    Alpha 010: -1 * correlation(rank(close), rank(volume), 3)
    """
    try:
        import pandas as pd

        ranked_close = df['close'].rank()
        ranked_volume = df['volume'].rank()
        corr = ranked_close.rolling(window=3).corr(ranked_volume)
        return -1 * corr
    except Exception as e:
        print(f"Error in alpha_010: {e}")
        return df['close'] * 0
