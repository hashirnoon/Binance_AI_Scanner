def bullish_choch(df):

    if len(df) < 20:
        return False

    recent = df.tail(10)

    # Previous Swing High
    previous_high = recent.iloc[:5]["High"].max()

    # Previous Swing Low
    previous_low = recent.iloc[:5]["Low"].min()

    # Latest Close
    last_close = recent.iloc[-1]["Close"]

    # Latest Low
    last_low = recent.iloc[-1]["Low"]

    # CHOCH
    if last_close > previous_high and last_low > previous_low:
        return True

    return False