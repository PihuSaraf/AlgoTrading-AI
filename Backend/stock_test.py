import yfinance as yf

stock = yf.download(
    "AAPL",
    period="5d"
)

print(stock)