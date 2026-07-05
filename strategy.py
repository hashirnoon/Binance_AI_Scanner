def check_buy_signal(data):

    score = 0
    reasons = []

    # ===== 4H Trend Filter =====
    if data["trend4h_ema50"] <= data["trend4h_ema200"]:
        return 0, 0, ["4H Trend Bearish"]
    
    # ===== 4H Trend =====
    if data["trend4h_ema50"] > data["trend4h_ema200"]:
        score += 20
        reasons.append("4H EMA Bullish")
   
    # ===== 1H Trend =====
    if data["trend_ema50"] > data["trend_ema200"]:
        score += 15
        reasons.append("1H EMA Bullish")

    # ===== 15m Trend =====
    if data["ema50"] > data["ema200"]:
        score += 10
        reasons.append("15m EMA Bullish")

    # ===== RSI =====
    if 30 <= data["rsi"] <= 45:
        score += 15
        reasons.append("RSI Buy Zone")

    # ===== Fibonacci =====
    fib618 = data["fib"]["0.618"]
    fib786 = data["fib"]["0.786"]

    if fib786 <= data["price"] <= fib618:
        score += 20
        reasons.append("Fib Buy Zone")

    # ===== Rejection =====
    if data["rejection"]:
        score += 20
        reasons.append("Bullish Rejection")

    # ===== BOS =====
    if data["bos"]:
        score += 15
        reasons.append("Bullish BOS")

    # ===== CHOCH =====
    if data["choch"]:
        score += 10
        reasons.append("Bullish CHOCH")

    # ===== Order Block =====
    if data["order_block"]:
        score += 10
        reasons.append("Bullish Order Block")  

    # ===== Fair Value Gap =====
    if data["fvg"]:
        score += 10
        reasons.append("Bullish FVG")  

    # ===== Liquidity =====
    if data["liquidity"]:
        score += 10
        reasons.append("Liquidity Sweep")
        
    # ===== Volume =====
    if data["volume"] > data["volume_ma"]:
        score += 10
        reasons.append("High Volume")

    confidence = min(score, 100)

    return score, confidence, reasons