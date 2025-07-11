def alpha_001(df):
    try:
        import numpy as np
        from scipy.stats import rankdata

        returns = df['returns']
        x = np.where(returns < 0, df['returns'].rolling(20).std(), df['close'])
        powered = np.power(x, 2)
        ranked = pd.Series(powered).rolling(5).apply(lambda x: rankdata(x)[-1] / len(x), raw=True)
        return ranked - 0.5
    except Exception as e:
        print(f"Error in alpha_001: {e}")
        return df['close'] * 0
