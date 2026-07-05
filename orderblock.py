def bullish_order_block(df):

    if len(df) < 10:
        return False

    recent = df.tail(10)

    # آخری Bearish Candle
    bearish = recent.iloc[-2]

    # آخری Bullish Candle
    bullish = recent.iloc[-1]

    if (
        bearish["Close"] < bearish["Open"]
        and bullish["Close"] > bullish["Open"]
        and bullish["Close"] > bearish["High"]
    ):
        return True

    return False