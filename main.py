import os
import time
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

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
