def alpha_002(df):
    try:
        import numpy as np

        log_volume = np.log(df['volume'].replace(0, np.nan))
        delta_log_volume = log_volume.diff(2)
        price_change = (df['close'] - df['open']) / df['open']

        ranked_x = delta_log_volume.rank()
        ranked_y = price_change.rank()

        return -1 * ranked_x.rolling(6).corr(ranked_y)
    except Exception as e:
        print(f"Error in alpha_002: {e}")
        return df['close'] * 0
