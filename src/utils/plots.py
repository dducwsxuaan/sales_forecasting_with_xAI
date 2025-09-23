import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales(df, store_id=1, item_id=1):
    """Plot sales and visualizing missing values"""

    df_2plot = df.query("(store_id == @store_id) & (item_id==@item_id)")
    store_name = df_2plot["store_name"].iloc[-1]
    item_name = df_2plot["item_name"].iloc[-1]

    fig, ax = plt.subplots(figsize=(6, 3))
    df_2plot[["date", "sales"]].plot(x="date", y="sales", ax=ax, legend=False)

    # Replace Nan Values with the last valid values
    nan_indices = df_2plot[df_2plot["sales"].isna()].index

    if len(nan_indices) >= 1:
        df_2plot = df_2plot.assign(sales=lambda df: df['sales'].fillna(method="ffill"))
        # Draw arrows for NaN values
        nan_dates = df_2plot.loc[nan_indices, "date"]
        nan_sales = df_2plot.loc[nan_indices, "sales"]
        for date, sales in zip(nan_dates, nan_sales):
            ax.annotate(
                "-",
                xy = (date, sales),
                color = "red",
                size=20
            )
    
    # Set plot labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.set_title(f"Store: {store_name} - Item: {item_name}")
    ax.legend()
    plt.show()