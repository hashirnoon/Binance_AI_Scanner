def bullish_bos(df):

    if len(df) < 10:
        return False

    recent = df.tail(6)

    previous_high = recent.iloc[:-1]["High"].max()

    last_close = recent.iloc[-1]["Close"]

    if last_close > previous_high:
        return True

    return False