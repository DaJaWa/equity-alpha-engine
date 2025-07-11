def alpha_005(df):
    try:
        import pandas as pd

        vwap_avg = df['vwap'].rolling(10).mean()
        term1 = (df['open'] - vwap_avg).rank()
        term2 = abs((df['close'] - df['vwap']).rank())
        return term1 * (-1 * term2)
    except Exception as e:
        print(f"Error in alpha_005: {e}")
        return df['close'] * 0
