import json
import os
from datetime import datetime

FILE = "signals.json"

COOLDOWN_MINUTES = 30


def load_signals():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)


def save_signals(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def already_sent(coin):

    data = load_signals()

    if coin not in data:
        return False

    last_time = datetime.fromisoformat(data[coin])

    minutes = (datetime.now() - last_time).total_seconds() / 60

    return minutes < COOLDOWN_MINUTES


def mark_sent(coin):

    data = load_signals()

    data[coin] = datetime.now().isoformat()

    save_signals(data)