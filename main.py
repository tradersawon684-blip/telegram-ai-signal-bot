from data import get_candles
from indicators import calculate_indicators
from strategy import generate_signal
from telegram_bot import send_message

PAIRS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD",
    "NZD/USD",
    "EUR/JPY",
    "GBP/JPY"
]


def main():
    for pair in PAIRS:

        candles = get_candles(pair)

        if candles is None:
            continue

        df = calculate_indicators(candles)

        signal = generate_signal(df)

        # Debug: NO TRADE হলেও Telegram-এ পাঠাবে
        if signal["signal"] == "NO TRADE":
            send_message(f"⚪ {pair}\nNO TRADE")
            continue

        message = f"""
🤖 AI BINARY SIGNAL BOT V0.1

{"🟢 BUY" if signal["signal"] == "BUY" else "🔴 SELL"}

💱 Pair: {pair}
⏰ Timeframe: 1 Minute

🎯 Entry:
Next Candle

⌛ Expiry:
1 Minute

📊 Analysis

✅ EMA Trend
✅ RSI Filter
✅ MACD Cross

🎯 Confidence:
{signal["confidence"]}

━━━━━━━━━━━━━━

Status:
🟢 VALID SIGNAL
"""

        send_message(message)

    print("Scan Complete")


if __name__ == "__main__":
    main()
