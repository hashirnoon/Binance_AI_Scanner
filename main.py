from scanner import scan_coin, get_usdt_symbols
from strategy import check_buy_signal
from discord_bot import send_discord

coins = get_usdt_symbols()

print(f"Scanning {len(coins)} Coins...\n")

for coin in coins:

    try:

        data = scan_coin(coin)

        score, confidence, reasons = check_buy_signal(data)

        if score >= 80:

            print("=" * 50)
            print("Coin       :", coin)
            print("Score      :", score)
            print("Confidence :", f"{confidence}%")
            print("Reasons:")

            for r in reasons:
                print("  ✅", r)

            trend4h = data["trend4h_ema50"] > data["trend4h_ema200"]
            trend1h = data["trend_ema50"] > data["trend_ema200"]
            trend15m = data["ema50"] > data["ema200"]

            print("4H Trend   :", trend4h)
            print("1H Trend   :", trend1h)
            print("15m Trend  :", trend15m)

            print("Rejection  :", data["rejection"])
            print("BOS        :", data["bos"])
            print("CHOCH      :", data["choch"])
            print("Order Block:", data["order_block"])
            print("FVG        :", data["fvg"])
            print("Liquidity  :", data["liquidity"])

            print()
            print("Trade Setup")
            print("-----------")
            print("Entry :", data["trade"]["entry"])
            print("SL    :", data["trade"]["sl"])
            print("TP1   :", data["trade"]["tp1"])
            print("TP2   :", data["trade"]["tp2"])
            print("TP3   :", data["trade"]["tp3"])

            message = f"""
🔥 ELITE BUY SIGNAL

🪙 Coin: {coin}

📊 Score: {score}
🎯 Confidence: {confidence}%

━━━━━━━━━━━━━━━━━━

📈 TREND

4H Bullish : {trend4h}
1H Bullish : {trend1h}
15m Bullish: {trend15m}

━━━━━━━━━━━━━━━━━━

💹 PRICE ACTION

Rejection   : {data['rejection']}
BOS         : {data['bos']}
CHOCH       : {data['choch']}
Order Block : {data['order_block']}
FVG         : {data['fvg']}
Liquidity   : {data['liquidity']}

━━━━━━━━━━━━━━━━━━

💰 TRADE SETUP

Entry : {data['trade']['entry']}
SL    : {data['trade']['sl']}
TP1   : {data['trade']['tp1']}
TP2   : {data['trade']['tp2']}
TP3   : {data['trade']['tp3']}

━━━━━━━━━━━━━━━━━━

🤖 Elite Binance AI Scanner
"""

            send_discord(message)

    except Exception as e:

        print(f"Error scanning {coin}: {e}")