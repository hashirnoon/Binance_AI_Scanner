from binance.client import Client

client = Client()

last_candle = None


def new_15m_candle():

    global last_candle

    kline = client.get_klines(
        symbol="BTCUSDT",
        interval=Client.KLINE_INTERVAL_15MINUTE,
        limit=1
    )

    candle_time = kline[0][0]

    if last_candle is None:
        last_candle = candle_time
        return False

    if candle_time != last_candle:
        last_candle = candle_time
        return True

    return False