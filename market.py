from scanner import scan_coin

def market_is_bullish():

    btc = scan_coin("BTCUSDT")

    trend4h = btc["trend4h_ema50"] > btc["trend4h_ema200"]
    trend1h = btc["trend_ema50"] > btc["trend_ema200"]

    return trend4h and trend1h