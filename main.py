
import requests
import time

BOT_TOKEN = "এখানে_আপনার_নতুন_BOT_TOKEN"
CHAT_ID = "এখানে_আপনার_CHAT_ID"

def send_signal(signal):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": signal
    }
    requests.post(url, data=data)

while True:
    send_signal("🟢 TEST SIGNAL\nPair: EUR/USD\nTimeframe: 1M\nAction: BUY")
    time.sleep(60)
