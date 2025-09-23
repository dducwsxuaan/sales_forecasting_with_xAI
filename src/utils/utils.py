import pickle

import lightgbm as lgbm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def fill_missing_values(df:pd.DataFrame):
    df_filled = df.copy()
    df_filled["sales"] = df_filled["sales"].fillna(df_filled["sales"].mean())
    return df_filled

def correct_outliers(df:pd.DataFrame, factor=3):
    """Identify and correct outliers in the 'sales' columns by reducing them to the mean"""
    df_corrected = df.copy()

    # Identify outliers using z-score
    z_scores = (df_corrected["sales"] - df_corrected["sales"].mean()) / df_corrected["sales"].std()
    outlier_indices = np.abs(z_scores) > factor
    # Correct outliers by reducing them to the mean
    df_corrected.loc[outlier_indices, "sales"] = df_corrected["sales"].mean()
    return df_corrected

def get_sample_stores(df:pd.DataFrame, store_id=1) -> pd.DataFrame:
    """Get the sample stores with store_id"""
    grouped = df.groupby("store_id")
    sample_store = grouped.get_group((store_id))
    return sample_store