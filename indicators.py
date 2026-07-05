import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

def calculate_indicators(df):

    df["EMA50"] = EMAIndicator(
        close=df["Close"],
        window=50
    ).ema_indicator()

    df["EMA200"] = EMAIndicator(
        close=df["Close"],
        window=200
    ).ema_indicator()

    df["RSI"] = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    df["Volume_MA"] = df["Volume"].rolling(20).mean()

    return df