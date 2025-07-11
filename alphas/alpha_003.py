def alpha_003(df):
    try:
        return -1 * df['open'].rank().rolling(10).corr(df['volume'].rank())
    except Exception as e:
        print(f"Error in alpha_003: {e}")
        return df['close'] * 0
