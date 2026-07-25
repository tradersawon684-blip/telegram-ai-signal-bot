import pandas as pd
import ta


def calculate_indicators(candles):
    df = pd.DataFrame(candles)

    df["close"] = df["close"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)

    # EMA
    df["EMA9"] = ta.trend.ema_indicator(df["close"], window=9)
    df["EMA21"] = ta.trend.ema_indicator(df["close"], window=21)

    # RSI
    df["RSI"] = ta.momentum.rsi(df["close"], window=14)

    # MACD
    macd = ta.trend.MACD(df["close"])
    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()

    return df
