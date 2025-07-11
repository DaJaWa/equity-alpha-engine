def alpha_020(df):
    """
    Alpha 020: -1 * rank(open - delay(close, 1)) * (open - close)
    """
    try:
        import pandas as pd

        delayed_close = df['close'].shift(1)
        open_minus_delayed = df['open'] - delayed_close
        ranked = open_minus_delayed.rank()
        result = -1 * ranked * (df['open'] - df['close'])

        return result
    except Exception as e:
        print(f"Error in alpha_020: {e}")
        return df['close'] * 0
