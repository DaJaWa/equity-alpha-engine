def alpha_101(df):
    """
    Alpha#101: (close - open) / ((high - low) + 0.001)
    Interpreted as a measure of intraday price movement relative to range.
    """
    alpha = (df['close'] - df['open']) / ((df['high'] - df['low']) + 0.001)
    return alpha
