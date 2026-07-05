from scanner import scan_coin

data = scan_coin("BTCUSDT")

print("Coin:", data["coin"])
print("Price:", data["price"])

print("\nSwing High:", data["fib"]["high"])
print("Swing Low :", data["fib"]["low"])

print("\nFib 0.382:", data["fib"]["0.382"])
print("Fib 0.500:", data["fib"]["0.500"])
print("Fib 0.618:", data["fib"]["0.618"])
print("Fib 0.786:", data["fib"]["0.786"])