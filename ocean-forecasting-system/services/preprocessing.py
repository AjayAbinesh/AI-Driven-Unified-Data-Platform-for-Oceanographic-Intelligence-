import pandas as pd

def clean_dataset(df):
    df.replace([99, 999, 9999, 999.0], pd.NA, inplace=True)
    df.dropna(inplace=True)

    df["timestamp"] = pd.to_datetime(
        df[["#YY", "MM", "DD", "hh", "mm"]]
    )

    df.sort_values("timestamp", inplace=True)

    # Lag feature
    df["lag_1"] = df["WVHT"].shift(1)
    df.dropna(inplace=True)

    return df