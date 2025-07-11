def alpha_006(df):
    """
    Alpha 006: -1 * correlation(open, volume, 10)
    """
    try:
        import pandas as pd
        return -1 * df['open'].rolling(10).corr(df['volume'])
    except Exception as e:
        print(f"Error in alpha_006: {e}")
        return df['close'] * 0
