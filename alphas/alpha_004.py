def alpha_004(df):
    try:
        from scipy.stats import rankdata

        return -1 * df['low'].rolling(9).apply(lambda x: rankdata(x)[-1] / len(x), raw=True)
    except Exception as e:
        print(f"Error in alpha_004: {e}")
        return df['close'] * 0
