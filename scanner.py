from binance.client import Client
import pandas as pd

from indicators import calculate_indicators
from fibonacci import fibonacci_levels
from rejection import bullish_rejection
from bos import bullish_bos
from choch import bullish_choch
from orderblock import bullish_order_block
from fvg import bullish_fvg
from liquidity import liquidity_sweep
from risk import calculate_trade_levels

client = Client()


def get_dataframe(symbol, interval):

    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=200
    )

    df = pd.DataFrame(
        klines,
        columns=[
            "Open Time",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Close Time",
            "Quote Asset Volume",
            "Trades",
            "Taker Buy Base",
            "Taker Buy Quote",
            "Ignore"
        ]
    )

    # Convert to float
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        df[col] = df[col].astype(float)

    # Indicators
    df = calculate_indicators(df)

    return df


def scan_coin(symbol="BTCUSDT"):

    # 15 Minute Entry Timeframe
    df15 = get_dataframe(
        symbol,
        Client.KLINE_INTERVAL_15MINUTE
    )

    # 1 Hour Trend Timeframe
    df1h = get_dataframe(
        symbol,
        Client.KLINE_INTERVAL_1HOUR
    )

    # 4 Hour Trend Timeframe
    df4h = get_dataframe(
        symbol,
        Client.KLINE_INTERVAL_4HOUR
    )
    # Latest Candle
    last = df15.iloc[-1]

    # Smart Fibonacci
    fib = fibonacci_levels(df15)

    # Rejection
    rejection = bullish_rejection(df15)

    # BOS
    bos = bullish_bos(df15)

    # CHOCH
    choch = bullish_choch(df15)

    # ORDER BLOCK
    order_block = bullish_order_block(df15)

    # FVG
    fvg = bullish_fvg(df15)

    # LIQUIDITY
    liquidity = liquidity_sweep(df15)

    # Trade Levels
    trade = calculate_trade_levels(df15)

    result = {

        "coin": symbol,

        # Price
        "price": last["Close"],

        # Entry Timeframe
        "ema50": last["EMA50"],
        "ema200": last["EMA200"],
        "rsi": last["RSI"],

        # Trend Timeframe (1H)
        "trend_ema50": df1h.iloc[-1]["EMA50"],
        "trend_ema200": df1h.iloc[-1]["EMA200"],

        # Higher Trend (4H)
        "trend4h_ema50": df4h.iloc[-1]["EMA50"],
        "trend4h_ema200": df4h.iloc[-1]["EMA200"],

        # Volume
        "volume": last["Volume"],
        "volume_ma": last["Volume_MA"],

        # Fibonacci
        "fib": fib,

        # Price Action
        "rejection": rejection,
        "bos": bos,
        "choch": choch,
        "order_block": order_block,
        "fvg": fvg,
        "liquidity": liquidity,
        "trade": trade,

    }

    return result


def get_usdt_symbols():

    exchange_info = client.get_exchange_info()

    symbols = []

    for s in exchange_info["symbols"]:

        if (
            s["quoteAsset"] == "USDT"
            and s["status"] == "TRADING"
            and s["isSpotTradingAllowed"]
        ):
            symbols.append(s["symbol"])

    return sorted(symbols)