import yfinance as yf
import pandas as pd

df = yf.download(
    "AAPL",
    period="1mo"
)

df["SMA_5"] = (
    df["Close"]
    .rolling(window=5)
    .mean()
)

print(
    df[
        ["Close","SMA_5"]
    ]
)