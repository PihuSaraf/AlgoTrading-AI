import yfinance as yf
from ta.momentum import RSIIndicator

# Download data
df = yf.download("AAPL", period="3mo")

# Extract Close prices
close_prices = df["Close"]["AAPL"]

# Calculate RSI
df["RSI"] = RSIIndicator(
    close=close_prices
).rsi()

# Get latest RSI value
latest_rsi = df["RSI"].dropna().iloc[-1]

# Generate recommendation
if latest_rsi < 30:
    signal = "BUY"

elif latest_rsi > 70:
    signal = "SELL"

else:
    signal = "HOLD"

print("Latest RSI:", round(latest_rsi, 2))
print("Recommendation:", signal)