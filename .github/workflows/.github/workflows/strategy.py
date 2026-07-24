def generate_signal(df):
    last = df.iloc[-1]

    ema9 = last["EMA9"]
    ema21 = last["EMA21"]
    rsi = last["RSI"]
    macd = last["MACD"]
    macd_signal = last["MACD_SIGNAL"]

    # BUY
    if (
        ema9 > ema21
        and rsi < 35
        and macd > macd_signal
    ):
        return {
            "signal": "BUY",
            "confidence": "Medium"
        }

    # SELL
    if (
        ema9 < ema21
        and rsi > 65
        and macd < macd_signal
    ):
        return {
            "signal": "SELL",
            "confidence": "Medium"
        }

    return {
        "signal": "NO TRADE",
        "confidence": "Low"
    }
