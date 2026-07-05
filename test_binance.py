from binance.client import Client
import pandas as pd

client = Client()

# 15m کی آخری 200 Candles
klines = client.get_klines(
    symbol="BTCUSDT",
    interval=Client.KLINE_INTERVAL_15MINUTE,
    limit=200
)

df = pd.DataFrame(
    klines,
    columns=[
        "Open Time","Open","High","Low","Close","Volume",
        "Close Time","Quote Asset Volume","Trades",
        "Taker Buy Base","Taker Buy Quote","Ignore"
    ]
)

# Numbers میں تبدیل کریں
df["High"] = df["High"].astype(float)
df["Low"] = df["Low"].astype(float)
df["Close"] = df["Close"].astype(float)

# Swing High اور Swing Low
high = df["High"].max()
low = df["Low"].min()

difference = high - low

fib_382 = high - (difference * 0.382)
fib_500 = high - (difference * 0.500)
fib_618 = high - (difference * 0.618)
fib_786 = high - (difference * 0.786)

price = df["Close"].iloc[-1]

print("Current Price:", price)
print("Swing High:", high)
print("Swing Low :", low)

print("\nFibonacci Levels")
print("0.382 =", fib_382)
print("0.500 =", fib_500)
print("0.618 =", fib_618)
print("0.786 =", fib_786)