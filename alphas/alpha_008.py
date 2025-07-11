def alpha_008(df):
    """
    Alpha 008: rank((Tsma(close, 5) - Tsma(close, 30)))
    """
    try:
        import pandas as pd
        short_sma = df['close'].rolling(window=5).mean()
        long_sma = df['close'].rolling(window=30).mean()
        diff = short_sma - long_sma
        ranked = diff.rank(pct=True)
        return ranked
    except Exception as e:
        print(f"Error in alpha_008: {e}")
        return df['close'] * 0
