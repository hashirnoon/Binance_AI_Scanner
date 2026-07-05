import requests

# اپنا Bot Token یہاں لکھیں
BOT_TOKEN = "8924734055:AAHznD7uygoCvNuULQVXN0_q7WPSYNVSctw"

# اپنی Chat ID یہاں لکھیں
CHAT_ID = "8676128672"


def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)