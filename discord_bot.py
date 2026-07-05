import requests

# اپنا Discord Webhook URL یہاں Paste کریں
WEBHOOK_URL = "https://discord.com/api/webhooks/1523262634298708028/lms_MFLhyqjhbWsgd8Ngu1m_LYtb7bRbUtCJI81y5QyjfwCuaCpV3zF-VVpgpQ4JFOLN"


def send_discord(message):

    payload = {
        "content": message
    }

    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        timeout=10
    )

    return response.status_code