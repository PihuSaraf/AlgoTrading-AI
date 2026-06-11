import yfinance as yf

df = yf.download(
    "AAPL",
    period="1mo"
)

df["EMA_5"] = (
    df["Close"]
    .ewm(span=5)
    .mean()
)

print(
    df[
        ["Close","EMA_5"]
    ]
)