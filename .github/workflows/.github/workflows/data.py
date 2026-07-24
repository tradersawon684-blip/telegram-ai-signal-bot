import requests
from config import API_KEY

BASE_URL = "https://api.twelvedata.com/time_series"


def get_candles(symbol, interval="1min", outputsize=100):
    url = (
        f"{BASE_URL}?symbol={symbol}"
        f"&interval={interval}"
        f"&outputsize={outputsize}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url, timeout=15)
    data = response.json()

    if "values" not in data:
        return None

    candles = list(reversed(data["values"]))
    return candles
