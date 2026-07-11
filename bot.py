import time
import subprocess
from datetime import datetime
from candle_checker import new_15m_candle

print("=" * 60)
print("🤖 Elite Binance AI Scanner Started")
print("=" * 60)

while True:

    if new_15m_candle():

        print()
        print("=" * 60)
        print("🕒 New 15m Candle Detected")
        print("=" * 60)

        try:
            subprocess.run(["python", "main.py"])

        except Exception as e:
            print("Error:", e)

    else:
        print("Waiting for next 15m candle...")

    time.sleep(20)