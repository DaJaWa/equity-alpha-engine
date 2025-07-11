def alpha_001(df):
    try:
        import numpy as np
        import pandas as pd
        from scipy.stats import rankdata

        # Ensure returns column exists
        if 'returns' not in df.columns:
            df['returns'] = df['close'].pct_change()

        # Compute conditional term
        rolling_std = df['returns'].rolling(20).std()
        x = np.where(df['returns'] < 0, rolling_std, df['close'])

        # Square the values
        powered = np.power(x, 2)

        # Build signal using rolling window ranking
        ranked = pd.Series(powered, index=df.index).rolling(5).apply(
            lambda x: rankdata(x)[-1] / len(x), raw=True
        )

        # Normalise signal
        signal = ranked - 0.5
        return signal

    except Exception as e:
        print(f"Error in alpha_001: {e}")
        return pd.Series(0, index=df.index)
