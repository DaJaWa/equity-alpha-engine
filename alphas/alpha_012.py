def alpha_012(df):
    """
    Alpha 012: SIGN(delta(close, 1)) * (high - close)
    """
    try:
        import numpy as np

        delta_close = df['close'].diff()
        sign = np.sign(delta_close)
        result = sign * (df['high'] - df['close'])

        return result
    except Exception as e:
        print(f"Error in alpha_012: {e}")
        return df['close'] * 0
