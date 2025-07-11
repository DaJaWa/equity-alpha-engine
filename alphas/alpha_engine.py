import os
import importlib
import pandas as pd

def apply_all_alphas(df, alpha_path="alphas"):
    alpha_signals = {}

    for filename in sorted(os.listdir(alpha_path)):
        if filename.startswith("alpha_") and filename.endswith(".py") and filename != "alpha_engine.py":
            alpha_name = filename.replace(".py", "")
            try:
                module = importlib.import_module(f"alphas.{alpha_name}")
                alpha_func = getattr(module, alpha_name)
                alpha_signals[alpha_name] = alpha_func(df)
            except Exception as e:
                print(f"Error in {alpha_name}: {e}")
    
    return pd.DataFrame(alpha_signals)
