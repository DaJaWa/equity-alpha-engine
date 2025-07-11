def alpha_019(df):
    """
    Alpha 019: -1 * (rank((open - close)) + rank((close - open)).rolling(5).mean())
    """
    try:
        import pandas as pd

        delta_oc = df['open'] - df['close']
        delta_co = df['close'] - df['open']

        rank_oc = delta_oc.rank()
        rank_co = delta_co.rank()

        mean_rank_co = rank_co.rolling(5).mean()
        result = -1 * (rank_oc + mean_rank_co)

        return result
    except Exception as e:
        print(f"Error in alpha_019: {e}")
        return df['close'] * 0
