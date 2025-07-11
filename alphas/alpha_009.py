def alpha_009(df):
    """
    Alpha 009: rank(open - Tsma(close, 5))
    """
    try:
        import pandas as pd
        diff = df['open'] - df['close'].rolling(window=5).mean()
        ranked = diff.rank(pct=True)
        return ranked
    except Exception as e:
        print(f"Error in alpha_009: {e}")
        return df['close'] * 0
