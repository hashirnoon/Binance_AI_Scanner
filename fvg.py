def bullish_fvg(df):

    if len(df) < 3:
        return False

    c1 = df.iloc[-3]
    c2 = df.iloc[-2]
    c3 = df.iloc[-1]

    # Bullish Fair Value Gap
    if c3["Low"] > c1["High"]:
        return True

    return False