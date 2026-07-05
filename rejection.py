def bullish_rejection(df):

    if len(df) < 3:
        return False

    last = df.iloc[-1]
    prev = df.iloc[-2]
    prev2 = df.iloc[-3]

    # -------- Hammer / Pin Bar --------
    body = abs(last["Close"] - last["Open"])

    lower_wick = min(last["Open"], last["Close"]) - last["Low"]
    upper_wick = last["High"] - max(last["Open"], last["Close"])

    hammer = (
        lower_wick > body * 2
        and upper_wick < body
    )

    # -------- Bullish Engulfing --------
    engulfing = (
        prev["Close"] < prev["Open"]
        and last["Close"] > last["Open"]
        and last["Open"] <= prev["Close"]
        and last["Close"] >= prev["Open"]
    )

    # -------- Morning Star --------
    morning_star = (
        prev2["Close"] < prev2["Open"]
        and abs(prev["Close"] - prev["Open"]) < abs(prev2["Close"] - prev2["Open"]) * 0.5
        and last["Close"] > last["Open"]
        and last["Close"] > (prev2["Open"] + prev2["Close"]) / 2
    )

    if hammer or engulfing or morning_star:
        return True

    return False