import yfinance as yf
from ta.momentum import RSIIndicator

# Download stock data
df = yf.download("AAPL", period="1mo")

# Extract Close prices
close_prices = df["Close"]["AAPL"]

# Calculate RSI
rsi = RSIIndicator(close=close_prices)

df["RSI"] = rsi.rsi()

# Show results
print(df[["RSI"]])