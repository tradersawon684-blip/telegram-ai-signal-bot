def generate_signal(df):
    last = df.iloc[-1]

    ema9 = last["EMA9"]
    ema21 = last["EMA21"]
    rsi = last["RSI"]
    macd = last["MACD"]
    macd_signal = last["MACD_SIGNAL"]

    # BUY
    if ema9 > ema21 and macd > macd_signal:
        confidence = "High" if rsi < 60 else "Medium"
        return {
            "signal": "BUY",
            "confidence": confidence
        }

    # SELL
    if ema9 < ema21 and macd < macd_signal:
        confidence = "High" if rsi > 40 else "Medium"
        return {
            "signal": "SELL",
            "confidence": confidence
        }

    return {
        "signal": "NO TRADE",
        "confidence": "Low"
    }
