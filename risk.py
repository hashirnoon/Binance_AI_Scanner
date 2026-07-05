import pandas as pd


def calculate_trade_levels(df):

    last = df.iloc[-1]

    entry = last["Close"]

    atr = (df["High"] - df["Low"]).rolling(14).mean().iloc[-1]

    stop_loss = entry - (atr * 1.5)

    tp1 = entry + (atr * 2)

    tp2 = entry + (atr * 3)

    tp3 = entry + (atr * 5)

    return {
        "entry": round(entry, 6),
        "sl": round(stop_loss, 6),
        "tp1": round(tp1, 6),
        "tp2": round(tp2, 6),
        "tp3": round(tp3, 6)
    }