def liquidity_sweep(df):

    if len(df) < 6:
        return False

    recent = df.tail(6)

    previous_low = recent.iloc[:-1]["Low"].min()

    last = recent.iloc[-1]

    # Price previous low کے نیچے گیا اور واپس اوپر بند ہوا
    if (
        last["Low"] < previous_low
        and last["Close"] > previous_low
    ):
        return True

    return False