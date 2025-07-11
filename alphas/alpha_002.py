def alpha_002(df):
    try:
        import numpy as np
        import pandas as pd

        # Replace zeros in volume to avoid log(0)
        log_volume = np.log(df['volume'].replace(0, np.nan))
        delta_log_volume = log_volume.diff(2)

        # Price change from open to close
        price_change = (df['close'] - df['open']) / df['open']

        # Drop NaNs before ranking to avoid shifting issues
        ranked_x = delta_log_volume.rank()
        ranked_y = price_change.rank()

        # Correlation over 6-day rolling window
        corr = ranked_x.rolling(6).corr(ranked_y)

        # Clean output
        signal = -1 * corr
        return signal

    except Exception as e:
        print(f"Error in alpha_002: {e}")
        return pd.Series(0, index=df.index)
