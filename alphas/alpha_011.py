def alpha_011(df):
    """
    Alpha 011: (close - open) / (high - low + 0.001)
    """
    try:
        return (df['close'] - df['open']) / (df['high'] - df['low'] + 0.001)
    except Exception as e:
        print(f"Error in alpha_011: {e}")
        return df['close'] * 0
