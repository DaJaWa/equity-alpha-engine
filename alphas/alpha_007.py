def alpha_007(df):
    """
    Alpha 007: If adv20 < volume, then -1 * delta(close, 7)
               Else, -1 * returns
    """
    try:
        import numpy as np
        import pandas as pd

        ret = df['returns']
        delta_close = df['close'].diff(7)
        condition = df['adv20'] < df['volume']
        result = np.where(condition, -1 * delta_close, -1 * ret)

        return pd.Series(result, index=df.index)
    except Exception as e:
        print(f"Error in alpha_007: {e}")
        return pd.Series(0, index=df.index)
