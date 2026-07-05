def find_swing_high_low(df, lookback=50):

    recent = df.tail(lookback)

    swing_high = recent["High"].max()
    swing_low = recent["Low"].min()

    return swing_high, swing_low


def fibonacci_levels(df):

    high, low = find_swing_high_low(df)

    diff = high - low

    return {
        "high": high,
        "low": low,
        "0.382": high - diff * 0.382,
        "0.500": high - diff * 0.500,
        "0.618": high - diff * 0.618,
        "0.786": high - diff * 0.786,
    }