from scanner import scan_coin, get_usdt_symbols
from strategy import check_buy_signal

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

            print("4H Trend   :", data["trend4h_ema50"] > data["trend4h_ema200"])
            print("1H Trend   :", data["trend_ema50"] > data["trend_ema200"])
            print("15m Trend  :", data["ema50"] > data["ema200"])

            print("Rejection  :", data["rejection"])
            print("BOS        :", data["bos"])
            print("CHOCH      :", data["choch"])
            print("Order Block:", data["order_block"])
            print("FVG        :", data["fvg"])
            print("Liquidity :", data["liquidity"])
            print()
            print("Trade Setup")
            print("-----------")
            print("Entry :", data["trade"]["entry"])
            print("SL    :", data["trade"]["sl"])
            print("TP1   :", data["trade"]["tp1"])
            print("TP2   :", data["trade"]["tp2"])
            print("TP3   :", data["trade"]["tp3"])

    except Exception as e:

        print(f"Error scanning {coin}: {e}")